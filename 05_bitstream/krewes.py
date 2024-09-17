file = open('krewes.txt','r')

readString = file.readline()

listOfNames = readString.split('@@@') # (pd$$$devo$$$ducky, ...)

dictionary = {4: {}, 5: {}}

for name in listOfNames:
    listOfPDD = name.split('$$$') # (pd, devo, ducky)
    
    
    