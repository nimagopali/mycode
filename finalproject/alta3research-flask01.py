#!/usr/bin/env python3

""" # at least two endpoints
    # at least one of your endpoints should return JSON
    # has ONE additional feature from the following list:
        one endpoint returns HTML that uses jinja2 logic
        requires a session value be present in order to get a response
        writes to/reads from a cookie
        reads from/writes to a sqlite3 database
"""

#!/usr/bin/env python3
"""DEMO: receiving JSON"""

from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
from flask import jsonify

app= Flask(__name__)

petdata= [{
      "name" : "Purrsloud",
      "species" : "Cat",
      "favFoods" : ["wet food", "dry food"],
      "birthYear" : 2016,
      "photo" : "https://learnwebcode.github.io/json-example/images/cat-2.jpg"
             }]

@app.route("/")
def index():
    return render_template("pet.html")

@app.route("/petdata")
def pet():
    # jsonify returns legal JSON
    return jsonify(petdata)

@app.route("/data", methods=["GET","POST"])
def data():
    if request.method == 'POST':
        data = request.json
        if data:
           data= json.loads(data)
           name = data["name"]
           species = data["species"]
           favFoods = data["favFoods"]
           birthYear = data["birthYEar"]
           photo = data["photo"]
           petdata.append({"name":name,"species":species,"favFoods":favFoods,"birthYear":birthYear, "photo":photo})

    return jsonify(petdata)

@app.route("/<petchoice>")
def greeting(petchoice):
    # render the jinja template "hellpetlover.html"
    # apply the value of petchoice for the var name
    return render_template("hellopetlover.html", pet = petchoice)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)

