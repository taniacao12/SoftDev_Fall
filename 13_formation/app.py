# Tania Cao
# SoftDev1 pd8
# K13 -- Echo Echo Echo 
# 2018-09-27

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('input.html')
    
@app.route("/auth")
def authenticate():
    username = request.args['username']
    method = request.method
    return render_template('output.html', user = username)

if __name__ == "__main__":
    app.debug = True
    app.run()
