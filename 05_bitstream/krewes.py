''' 
Jayden Zhang, Endrit Idrizi 
J.E.D
SoftDev
K05 -- Reading Files, Spliting Strings, Creating Dictionaries / Using open() to open a file, split() to split a string into an array, making a list of dictionaries using append().
2024-09-17
time spent: 0.7 hours 
'''

import random

file = open('krewes.txt','r')

readString = file.readline()
listOfNames = readString.split('@@@') # (pd$$$devo$$$ducky, ...)
list = []

for name in listOfNames:
    listOfPDD = name.split('$$$') # (pd, devo, ducky)
    list.append({'PD': listOfPDD[0], 'devo': listOfPDD[1], 'ducky': listOfPDD[2]}) # adds a dictonary to the list

randomInt = random.randint(0, len(list) - 1) # chooses a random index within the list of dictionaries.
devo = list[randomInt]["PD"] # finds the devo value of the random dictionary
period = list[randomInt]['devo'] # finds the period value of the random dictionary
ducky = list[randomInt]['ducky'] # finds the ducky value of the random dictionary

print(devo, period, ducky) # prints a random devo, period, and ducky

    
    
    