from flask import Flask, render_template, request, redirect, url_for, session, g
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'

DATABASE = 'blog.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
        
def init_db():
    """Creates tables if they do not exist"""
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        
        # Create Users Table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        ''')

        # Create Blogs Table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS blogs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                title TEXT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
            )
        ''')

        # Create Entries Table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS entries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                blog_id INTEGER NOT NULL,
                content TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (blog_id) REFERENCES blogs(id) ON DELETE CASCADE
            )
        ''')

        conn.commit()
    print("Database initialized successfully!")

with app.app_context():
    """Initialize the database before the first request"""
    init_db()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        db.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        db.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        user = db.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password)).fetchone()
        if user:
            session['user_id'] = user['id']
            return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('home'))

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    db = get_db()
    blogs = db.execute('SELECT * FROM blogs WHERE user_id = ?', (session['user_id'],)).fetchall()
    return render_template('dashboard.html', blogs=blogs)

@app.route('/new_blog', methods=['GET', 'POST'])
def new_blog():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        title = request.form['title']
        db = get_db()
        db.execute('INSERT INTO blogs (user_id, title) VALUES (?, ?)', (session['user_id'], title))
        db.commit()
        return redirect(url_for('dashboard'))
    return render_template('new_blog.html')

@app.route('/blog/<int:blog_id>', methods=['GET', 'POST'])
def blog(blog_id):
    db = get_db()
    blog = db.execute('SELECT * FROM blogs WHERE id = ?', (blog_id,)).fetchone()
    if request.method == 'POST':
        content = request.form['content']
        db.execute('INSERT INTO entries (blog_id, content) VALUES (?, ?)', (blog_id, content))
        db.commit()
    entries = db.execute('SELECT * FROM entries WHERE blog_id = ?', (blog_id,)).fetchall()
    return render_template('blog.html', blog=blog, entries=entries)

if __name__ == '__main__':
    app.run(debug=True)
