'''
Jayden Zhang, Endrit Idrizi
SoftDev
K08 -- Teardown -- Discovering Flask and where we have seen it before.
2024-09-20
time spent: 0.2 hours
'''

'''
DISCO:
- print() outputs to the terminal.
- return outputs to the localhost page created.
- Flask uses similar syntax to other programming languages like Java or JS.
- Flask uses a .run method to run the program.

QCC:
0. Java and JS. To initate a new object you would assign it to a constructor. In this case, it would be the "Flask" Constructer.
1. In the home directories, navigation is controlled through using the '/'. In html pages, '/' is also a key element to switch between the pages. Typically, '/' by itself represents the home directory.
2. This line prints to the terminal. It will print "__main__" or otherwise the name of the module (as per the Flask documentation).
3. __main__
4. It will print it out as html code. When you click on the local host link provided, "No hablo queso!" is shown on the page.
5. We've seen similar constructs in languages that initalize a server such as in JS when you're trying to build a web application.
 ...

INVESTIGATIVE APPROACH:
We first created a virtual environemnt to download the import of Flask. Then, we used python3 app.py to run the file and produce results. We followed any outputs in the terminal including the localhost links to come up with answers to the following questions. We also used the help of Flask documentation to further help me understand anything we were stuck on.
'''


from flask import Flask

app = Flask(__name__)                    # Q0: Where have you seen similar syntax in other langs?

@app.route("/")                          # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__)                      # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"             # Q4: Will this appear anywhere? How u know?

app.run()                                # Q5: Where have you seen similar constructs in other languages?



