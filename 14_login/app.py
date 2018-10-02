#Team pengWin: Maryann Foley and Tania Cao
#SoftDev1 pd8
#K14 -- Do I Know You?
#2018-10-02    

from flask import Flask, render_template, request,session,url_for,redirect
import os
import csv
app = Flask(__name__)

app.secret_key=os.urandom(32)

@app.route("/", methods=['POST',"GET"])
def home():
	if session.get("uname"):
		return render_template("welcome.html")
	return render_template("login.html",Title = 'Login')

@app.route("/auth", methods=['POST'])
def auth():
	givenUname=request.form["username"]
	givenPwd=request.form["password"]
	if givenUname=="usr": 
		if givenPwd=="pwd":
			session["uname"]=givenUname
			if session.get("error"):
				session.pop("error")
		else:
			session["error"]=2#error 2 means password was wrong
		return redirect(url_for("home"))
	else:
		session["error"]=1
		return redirect(url_for("home"))#error 1 means username was wrong

@app.route("/logout", methods=['POST',"GET"])
def logout():
	if session.get("uname"):
		session.pop("uname")
		print(session)
	return redirect(url_for("home"))

if __name__ == "__main__":
    app.debug = True
    app.run()
