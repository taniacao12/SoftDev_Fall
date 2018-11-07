from flask import Flask, render_template, request, session
import os

app=Flask(__name__)

app.secret_key = os.urandom(32)
session["hello"]="pass1";

@app.route('/')
def disp_login():
    return render_template('test.html')

@app.route('/auth')
def authenticate():
    print(url_for('disp_login'))
    return render_template('login.html')

if __name__ == "__main__":
    app.debug = True
    app.run()
