'''
JED - Jayden Zhang, Endrit Idrizi
SoftDev
K16 - Flask-Sessions - Creating a Flask Session to store usernames to automatically log-in without having to type the credentials.
2024-10-15
time spent: 2 hrs
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
    if 'username' in session: # if the username is still present in the session (hasn't logged out)
        return render_template("response.html", username=session['username']) # logIn without entering credentials
    return render_template('login.html') # else, signUp again.


@app.route("/signUp", methods=['GET'])
def signUp():
    username = request.args.get("username") # get the inputed username
    session['username'] = username # store it in session

    return render_template("response.html", username=session['username'])

@app.route("/logOut", methods=['GET']) 
def logOut():
    session.clear() # clears the session when you logOut
    return render_template("logout.html")


if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.secret_key = os.urandom(32)
    app.debug = True 
    app.run()
