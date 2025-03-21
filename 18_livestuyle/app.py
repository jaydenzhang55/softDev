'''
JED - Jayden Zhang, Endrit Idrizi
SoftDev
K18 - LiveStuyle - Adding Flask and HMTL + CSS together to create a live page of our creation!!! 
2024-10-16
time spent: 1 hrs
'''

# import conventions:
# list most general first (standard python library)
# ...then pip installs (eg Flask)
# ...then your own home-rolled modules/packages (today's test module)

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object

@app.route("/")
def notes():
    return open("readme.md", 'r') # readme file

@app.route("/website")
def disp_webpage():
    return render_template('index.html') # website file

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
