#!/usr/bin/python3
"""Alta3 APIs and HTML"""

from flask import Flask
from flask import redirect
from flask import request
from flask import render_template
from flask import url_for

app = Flask(__name__)

# landing page("/") return an HTML from

@app.route("/")
def start():
    return render_template("trivia.html")

# correct page
@app.route("/correct")
def success():
    return "Cogratulation! You got it right!"

# answer posting page
# if the answer is correct, the user is redirected to success("/correct") route
# if the answer is incorrect, the user is returned to the form to try again
@app.route('/login', methods=['GET','POST'])
def guess():
    if request.method=='POST':
        if request.form.get('nm') and request.form.get('nm')=='The Pacific Ocean'.lower():
            return redirect(url_for('success'))
        else:
            return redirect(url_for('start'))
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
