# Team PandaBearBBT - Tania Cao Su and Zane Wang
# SoftDev1 pd8
# K17 -- Average
# 2018-10-05 F

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#searches database for students, courses the student is in, and the grade the
#student has gotten in that course
def searchGrades():
    command = "SELECT {0},{1},{2} FROM {3},{4} WHERE {5} = {6}".format("name","code","mark","peeps_info","courses_info","peeps_info.id","courses_info.id")
    c.execute(command)
    print("ALL STUDENTS WITH THE CLASSES THEY ARE TAKING AND THEIR CORRESPONDING GRADES IN THOSE CLASSES:")
    for row in c:
        print(row)
    return c

#calc avg of students, makes a list of students and their corresponding ids
def makeAvgTable():
    sumlist = {}
    courselist = {}

    command = "DROP TABLE IF EXISTS peeps_avg"
    c.execute(command)

    command = "CREATE TABLE peeps_avg(id INTEGER, avg INTEGER)"
    c.execute(command)
    
    #list of all marks per id
    command = "SELECT {0},{1} FROM {2},{3} WHERE {4} = {5}".format("peeps_info.id","mark","peeps_info","courses_info","peeps_info.id","courses_info.id")
    c.execute(command)
    print("ALL THE SELECTED ROWS IN C")
    for row in c:
        print(row)
        if row[0] in sumlist:
            sumlist[row[0]] += row[1]
            courselist[row[0]] += 1
        else:
            sumlist[row[0]] = row[1]
            courselist[row[0]] = 1
    for id in courselist:
        avg = sumlist[id] / courselist[id]
        command = 'INSERT INTO peeps_avg VALUES({0}, {1})'.format(id, avg)
        c.execute(command)

#selects the name, id, and avgs of all students, so that they can be displayed using the main method later
def displayAvg():
    command = "SELECT {0},{1},{2} FROM {3},{4} WHERE {5} = {6}".format("name","peeps_info.id","avg","peeps_info","peeps_avg","peeps_info.id","peeps_avg.id",)
    c.execute(command)
    print("ALL STUDENTS AND THEIR AVERAGES")
    for row in c:
        print(row)
    return c

def main():
    searchGrades()
    makeAvgTable()
    #run display to set c as the one from displayAvg()
    displayAvg()

main()

db.commit() #save changes
db.close() #close database
