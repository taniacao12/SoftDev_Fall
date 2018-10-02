# Tania Cao
# SoftDev1 pd8
# K13 -- Echo Echo Echo 
# 2018-09-27

from flask import Flask, render_template, request, session, url_for, redirect
import os, csv
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('input.html')
    
@app.route("/login")
def login():
    username = request.form['user']
    password = request.form['pass']
    
    file = open ('data/account.csv', 'rU')
    content = file.read ()
    content = content.split ('\n')
    account = []
    for element in content:
        account.append (element.split (','))
    for element in account:
        if element[0] == username and element[1] == password:
            return render_template('output1.html', user = username)
    return render_template('output2.html')

if __name__ == "__main__":
    app.debug = True
    app.run()
