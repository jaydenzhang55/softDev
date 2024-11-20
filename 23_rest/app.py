import flask, render_template, urllib.request, json

@app.route('/', methods=)
def home():
    data = urllib.request.urlopen('')
    dictionary = json.load(data.read())
    