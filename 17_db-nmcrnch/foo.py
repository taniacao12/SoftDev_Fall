#azrael - Jason Tung and Zane Wang
#SoftDev1 pd8
#K16 -- No Trouble
#2018-10-04

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE

command = 'CREATE TABLE peeps_info (name TEXT, age INTEGER, id INTEGER);'

c.execute(command)

command = 'CREATE TABLE courses_info (code TEXT, mark INTEGER, id INTEGER);'

c.execute(command)

with open('peeps.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        command = 'INSERT INTO peeps_info VALUES ("' + row['name'] + '", ' + row['age'] + ', ' + row['id'] + ');'
        c.execute(command)

with open('courses.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        command = 'INSERT INTO courses_info VALUES ("' + row['code'] + '", ' + row['mark'] + ', ' + row['id'] + ');'
        c.execute(command)



#build SQL stmt, save as string
#c.execute(command)    #run SQL statement


#==========================================================

db.commit() #save changes
db.close() #close database
