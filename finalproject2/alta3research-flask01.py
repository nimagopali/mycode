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
from flask import make_response
from flask import url_for
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

@app.route("/setcookie", methods = ["POST", "GET"])
def setcookie():
    # if user generates a POST to our API
    if request.method == "POST":
        if request.form.get("nm"): # if nm was assigned via the POST
            pet = request.form.get("nm") # grab the value of nm from the POST
        else: # a post without nm then assign value defaultuser
            pet = "cat"

        # Note that cookies are set on response objects.
        # Since you normally just return strings
        # Flask will convert them into response objects for you
        resp = make_response(render_template("readcookie.html"))
        # add a cookie to our response object
                        #cookievar #value
        resp.set_cookie("petChoice", pet)

        # return our response object includes our cookie
        return resp

    if request.method == "GET": # if the user sends a GET
        return redirect(url_for("index")) # redirect to index

# cookie for their petChoice
@app.route("/getcookie")
def getcookie():
    # attempt to read the value of petChoice from user cookie
    petChoice = request.cookies.get("petChoice") # 

    # return HTML embedded with petChoice (value of petChoice read from cookie)
    return f'<body style="background-color:black; color:white; text-align:center;"><h1>Welcome {petChoice} lover!</br><h3 style="color:red;">To know about the {petChoice} fact, go to the /{petChoice} route!</h3></h1></body>'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
