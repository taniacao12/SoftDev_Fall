from flask import Flask, render_template
import json, urllib.request
app = Flask(__name__)

@app.route("/")
def home():
    u = urllib.request.urlopen("https://api.nasa.gov/planetary/apod?api_key=JqCRPvo09gUFdEdfnYg8hzmV96jFWGkKqVSfHfZS")
    content = u.read()
    info = json.loads(content)
    des = info["title"]
    img = info["url"]
    return render_template("url.html", img = img, title = des)

if __name__ == "__main__":
    app.debug = True
    app.run()
