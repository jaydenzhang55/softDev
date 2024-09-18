file = open('krewes.txt','r')

readString = file.readline()

listOfNames = readString.split('@@@') # (pd$$$devo$$$ducky, ...)

list = []

for name in listOfNames:
    listOfPDD = name.split('$$$') # (pd, devo, ducky)
    print(listOfPDD)
    list.append({'PD': listOfPDD[0], 'devo': listOfPDD[1], 'ducky': listOfPDD[2]})

print(list)

    
    
    