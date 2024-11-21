'''
NJ - Jayden Z., Naf M.
SoftDev
K23 -- Learning About and Using Rest APIs (Specifically NASA's API)
2024-11-21
time spent: 0.5
'''

import urllib.request, json
from flask import Flask, render_template

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def home():
    key = 'https://api.nasa.gov/planetary/apod?api_key=Ya7bZqbUfdbrFDXPnWr3sTUPj9g09UwFrBtjkcqn'
    data = urllib.request.urlopen(key) # grabs the json file from the website.
    dictionary = json.loads(data.read()) # translates the json file into a python dictionary.
    hdurl = dictionary.get('hdurl') # grabs the value from the hdurl key.
    description = dictionary.get('explanation') # grabs the value from the explanation key.
    return render_template('main.html', photo=hdurl, description=description)

if __name__ == "__main__":
    app.debug = True 
    app.run()