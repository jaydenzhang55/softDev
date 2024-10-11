'''
JED - Jayden Zhang, Endrit Idrizi
SoftDev
K16 - Flask-Form - Learning and Experimenting with Flask GET and POST Methods.
2024-10-9
time spent: 1 hrs
'''

# import conventions:
# list most general first (standard python library)
# ...then pip installs (eg Flask)
# ...then your own home-rolled modules/packages (today's test module)

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission
from flask import session
import os

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object

@app.route("/", methods=['GET', 'POST'])
def disp_loginpage():
    return render_template('login.html')


@app.route("/signUp", methods=['GET'])
def signUp():
    gvp = "The difference between the GET and POST methods lies in the way data is retrieved. GET checks the dictionary (args) for a key that matches the input, while POST essentially pushes your data to the servers POST dictionary (form). Both are sent as QueryStrings REQUESTS."
    session['username'] = request.cookies.get('username')
    session['password'] = request.cookies.get('password')

    print(request.cookies.get('username'))
    print(request.cookies.get('password'))

    return render_template("response.html", username=session['username'], gvp=gvp)

@app.route("/logIn", methods=['GET'])
def logIn():
    gvp = "The difference between the GET and POST methods lies in the way data is retrieved. GET checks the dictionary (args) for a key that matches the input, while POST essentially pushes your data to the servers POST dictionary (form). Both are sent as QueryStrings REQUESTS."
    username = request.args["username"] # GET uses request.form.
    app.secret_key = os.urandom(32)

    return render_template("response.html", username="dsajhsdlkj", gvp=gvp)

@app.route("/logOut", methods=['GET'])
def logOut():
    username = request.args["username"] # GET uses request.form.
    app.secret_key = os.random(32)

    return render_template("logout.html")


if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.secret_key = os.urandom(32)
    app.debug = True 
    app.run()
