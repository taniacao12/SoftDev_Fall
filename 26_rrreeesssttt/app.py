from flask import Flask, render_template
import json, urllib.request, random
app = Flask(__name__)

@app.route("/")
def home():
    breeds = "https://catfact.ninja/breeds"
    facts = "https://catfact.ninja/fact"
    bd = urllib.request.urlopen(breeds)
    ft = urllib.request.urlopen(fact)
		b = bd.read()
		f = ft.read()
    breed = json.loads(b)
		fact = json.loads(f)
    breed = breed["data"]
		fact = fact["fact"]
    return render_template("url.html", breed = breed, fact = fact)

if __name__ == "__main__":
    app.debug = True
    app.run()
