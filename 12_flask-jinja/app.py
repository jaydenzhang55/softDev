# Endrit Idrizi, Jayden Zhang
# JED
# SoftDev
# Sep 2024

'''
Notes:
- You're able to import template files and use them in methods to
fill in any variables within the template file.
- You can't use thonny to edit HTML files (or open one at least).
- Endfor in HTML is used to end for loops in HTML code.
'''

"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Q0:
Removing render_template wouldn't affect the @app.route('/'),
but would rather affect the function that uses render_template. It would
most likely result in an error because you're not able to return a method
that isn't imported or previously defined. 

Q1:
Yes, the url would be http://localhost:5000/my_foist_template or
https://127.0.0.1:5000/my_foist_template as it redirects the page to
that app.route function.

Q2:
model_template.html is the template file that contains the HTML
to which collection and foo are used as the values of the objects
(otherwise in {{}}) within the html file.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Q0: What will happen if you remove render_template from the following statement?
# (log prediction before executing...)   
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "No hablo queso!"

coll = [0,1,1,2,3,5,8]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Q1: Can all of your teammates confidently predict the URL to use to load this page?
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route("/my_foist_template") 
def test_tmplt():
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Q2: What is the significance of each argument? Simplest, most concise answer best.
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    return render_template( 'model_tmplt.html', foo="fooooo", collection=coll)


if __name__ == "__main__":
    app.debug = True
    app.run()
