# JED - Jayden Zhang, Endrit Idrizi
# SoftDev
# K19 - csv2db - Creating a SQL Database Using CSV Values
# 2024-10-21
# time spent: 1 hrs

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O

DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================

c.execute("DELETE FROM students") # clears pre-existing data from the table. IF NOT: "sqlite3.IntegrityError: UNIQUE constraint failed: students.id"
c.execute("DELETE FROM courses") # clears pre-existing data from the table. IF NOT: "sqlite3.IntegrityError: UNIQUE constraint failed: courses.id"

with open('students.csv', newline='') as csvfile: # opens the CSV file
    studentsCSV = csv.DictReader(csvfile) # puts the data into a dictionary
    for studentRow in studentsCSV:
        name = studentRow['name']
        age = studentRow['age']
        id = studentRow['id']
        c.execute("INSERT INTO students (name, age, id) VALUES (?, ?, ?)", (name, age, id)) # inserts the values of each key into the table

with open('courses.csv', newline='') as csvfile: # opens the CSV file
    coursesCSV = csv.DictReader(csvfile)
    for courseRow in coursesCSV:
        code = courseRow ['code']
        mark = courseRow['mark']
        # id = courseRow['id'] # IDs that are the same throw errors.
        c.execute("INSERT INTO courses (code, mark) VALUES(?, ?)", (code, mark)) # inserts the values of key each into the table

command1 = "SELECT * FROM students;"   # test SQL stmt in sqlite3 shell, save as string
c.execute(command1)    # run SQL statement

command2 = "SELECT * FROM courses;"   # test SQL stmt in sqlite3 shell, save as string
c.execute(command2)    # run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database
