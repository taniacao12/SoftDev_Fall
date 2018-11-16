from flask import Flask, render_template
import json, urllib.request, random
app = Flask(__name__)

@app.route("/")
def home():
    # CAT FACTS ---------------------------------------------------------------------------
    fact = json.loads(urllib.request.urlopen("https://catfact.ninja/fact").read())
    fact = fact["fact"]
    ubreed = "https://catfact.ninja/breeds?limit=1&page="
    breeds = []
    for num in range(5):
        dbreed = json.loads(urllib.request.urlopen(ubreed + str(random.randint(1,99))).read())
        breeds += dbreed["data"]

    # RANDOM POEMS ------------------------------------------------------------------------
    poems = json.loads(urllib.request.urlopen("https://www.poemist.com/api/v1/randompoems").read())
    poem = poems[random.randint(0,5)]

    # WIKIPEDIA ---------------------------------------------------------------------------
    advice = json.loads(urllib.request.urlopen("https://api.adviceslip.com/advice").read())
    advice = advice["slip"]
    
    return render_template("url.html", fact = fact, breeds = breeds, poem = poem, advice = advice)

if __name__ == "__main__":
    app.debug = True
    app.run()
    
