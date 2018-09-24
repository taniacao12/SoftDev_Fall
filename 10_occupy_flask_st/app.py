# Tania Cao
# SoftDev1 pd8
# K10 -- Jinja Tuning
# 2018-09-23

from flask import Flask, render_template
import random
import csv

app = Flask(__name__)

coll = {}
    
def makeDict():
    dict = {}
    with open('data/occupations.csv', 'rt') as csvfile:
        reader = csv.reader(csvfile)
        for i in reader:
            dict[i[0]] = float(i[1])
    return dict
    
def occ():
    dict = makeDict()
    del dict['Occupations']
    del dict['Total']
    jobs = list(dict.keys())
    fate = random.choices(jobs, dict.values())[0]
    return fate
    
@app.route("/occupations")
def run():
    return render_template ("template.html",
           title = "Occupations",
           collection = makeDict(),
           random = occ())
    
if __name__ == "__main__":
    app.debug = True
    app.run()
