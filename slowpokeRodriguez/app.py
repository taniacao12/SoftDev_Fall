import os, csv, time, sqlite3

from flask import Flask, render_template, request,session,url_for,redirect,flash

app = Flask(__name__)

app.secret_key = os.urandom(32) #key for session

user = "a"
passw = "b"

@app.route("/")
def home():
    if "logged_in" in session:
        return redirect(url_for("home"))
    return render_template("home.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/auth")
def auth():
    if user == request.args["username"] and passw == request.args["password"]:
        session["logged_in"] = request.form["user"]
        return redirect(url_for("home"))

    flash("Username or password is incorrect")
    return render_template("login.html")


    return redirect(url_for("home"))

if __name__ == "__main__":
    app.debug = True
    app.run()
