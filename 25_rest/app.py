from flask import Flask, render_template
import json, urllib.request
app = Flask(__name__)

@app.route("/")
def home():
    u = urllib.request.urlopen("https://holidayapi.com/v1/holidays?key=95545be2-f15f-4cda-9a81-682b026965c4&country=US&year=2017&month=11")
    content = u.read()
    info = json.loads(content)
    content = info["holidays"]
    return render_template("url.html", content = content)

if __name__ == "__main__":
    app.debug = True
    app.run()
