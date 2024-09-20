'''
Endrit Idrizi, Jayden Zhang
JED
SoftDev
K06 -- Divine your destiny/ Reading CSV and weighted distribution/ Using open to read a csv file, turning it into a dictionary, and then using a random number generator to get a specific weighted average.
2024-9-19
time spent: 1 hour
'''

'''
Disco:
- Import csv as a module.
Q: 
- What are more efficient ways to write a weighted average generator?
- What other primitive file types are there?
- Is there a way to omit the first and last rows of the csv file without having to explicitly do it?
- What other file types can you read and open? What is the extent to Python libraries when it comes to file types?
- Is there a stastical model that can show the distrubution of this weighted average situation?
C:
- Dictionaries in Python have certain methods like update and items that you can use.
- To cast, you have to add the keyword with parenthesis like float(...).
- The with, as statement is essentially a better way of error handling with files (right?).
C:
- If you had a long dictionary, would this cause a hiccup in processing speed? 
- Can we use an algorithm to make the program more efficient?
HOW THIS SCRIPT WORKS:
- Opens the csv file using csv.reader and excludes the first and last row. Creates a range of random numbers each with a chance equal to each occupation's percentage.
'''

import csv
import random
with open('occupations.csv', newline='') as csvfile: # reads the csv file using python's csv import
    occupations = csv.reader(csvfile)
    dict = {} # initatizes a new dictionary
    for row in occupations:
        if (row[0] != 'Job Class') and (row[0] != 'Total'): # removes the first and last keys
            dict.update({row[0]:float(row[1])}) # updates the dictionary with the occupations as keys and the percentage as values.
    
def randomSelection(): # function for choosing a random number with a weighted percentage
    x = random.uniform(0.0,99.8)
    for key, value in dict.items():
        x = x - value # each key has a range and this subtracts until it is chosen
        if x <= 0:
            print(key)
            break
    
# Test Case
randomSelection() # doing this x->infinity times will create a distrubution similar to the weighted average