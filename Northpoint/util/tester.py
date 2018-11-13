import sqlite3   
import csv
import time

DB_FILE="../northpoint.db"

db = sqlite3.connect(DB_FILE) 
c = db.cursor()   
# change total_stories to number stories you want in db
total_stories = 20

c.execute("CREATE TABLE IF NOT EXISTS stories (story_id INTEGER, name TEXT, edit TEXT, editor TEXT, timestamp INTEGER)")

with open('../data/stories.csv') as file:
    list = csv.reader(file)
    for row in list:
        if total_stories == 0:
            break
        info = [int(row[0]), row[1], row[2], row[3], int(time.time())]
        c.execute("INSERT INTO stories VALUES(?,?,?,?,?)", info)
        total_stories -= 1
        
db.commit()
db.close()