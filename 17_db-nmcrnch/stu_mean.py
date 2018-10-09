# Team PandaBearBBT - Tania Cao Su and Zane Wang
# SoftDev1 pd8
# K17 -- Average
# 2018-10-05 F

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

command = "SELECT * FROM {}".format("peeps_info;")
c.execute(command)

for row in c:
    print(row)

db.commit() #save changes
db.close() #close database
