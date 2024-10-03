'''
Margie Cao, Jayden Zhang, Nafiyu Murtaza
GOOGle
SoftDev
K13 -- Combine -- Creating a table of occupations with links to each one and using render_template to display templates on certain routes. Also, using everything we've learned before to create the page. 
2024-09-30
Time Spent: 3hrs
'''

import csv, random

with open('data/occupations.csv', newline='') as csvfile: # reads the csv file using python's csv import
    occupations = csv.reader(csvfile)
    dict = {} # initatizes a new dictionary
    usedDict = {}
    for row in occupations:
        if (row[0] != 'Job Class') and (row[0] != 'Total'): # removes the first and last keys
            dict.update({row[0]:[float(row[1]), row[2]]}) # updates the dictionary with the occupations as keys and a list containing the percentage and link as values.
            usedDict.update({row[0]:[float(row[1]), row[2]]})
        else:
            dict.update({row[0]:[row[1], row[2]]})
    
from flask import Flask, render_template # render_template is an import from flask
app = Flask(__name__) # assigns the Flask constructor to variable app

@app.route("/") # home route
def starting_page():
    return open('notes.txt', mode='r') # returns note.txt in the home route

@app.route("/wdywtbwygp") # the wdywtbwygp route gives a tabulated list of occupations, percentages, and a link to them. Also includes a random occupation.
def occupations():
    chosenOccupation = "Occupation of the Day: " # starting text for the random occupation.
    ourTNPG = "GOOGle - Margie Cao, Jayden Zhang, Nafiyu Murtaza" # creates the TNPG
    heading = "Below are links that describe each of most POPULAR occupations! We also provide a free occupation generator to get YOU started!!!" # description about the page
    x = random.uniform(0.0,99.8) # random float from 0.0 to 99.8
    for key, value in usedDict.items():
        x = x - value[0] # each key has a range and this subtracts until it is chosen
        if x <= 0:
            chosenOccupation = chosenOccupation + key # adds the randomly selected occupation to the chosenOccupation variable
            break
    return render_template("template.html", title="Find the Occupation that Suits YOU!", ourTNPG=ourTNPG, chosenOccupation=chosenOccupation, descriptiveHeading=heading, newCollection=usedDict.items(), topAndBottom=dict, keys=list(dict.keys())) # constructs the HTML page using the parameters to update the HTML variables.

if __name__ == "__main__": 
    app.debug = True # allows for constant refreshing
    app.run() # runs the app