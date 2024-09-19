import csv
with open('occupations.csv', newline='') as csvfile:
    occupations = csv.reader(csvfile)
    dictionary = {}
    for row in occupations:
        dictionary[row[0]] = row[1]
    print(dictionary)
        
        
