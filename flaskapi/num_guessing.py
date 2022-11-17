#!/usr/bin/env python3

from flask import Flask
# needs a ./templates dir
from flask import render_template

app=Flask(__name__)

# add an int variable to the URL
@app.route('/scoretest/<int:score>')
def index(score):
    # render the template with the num guess
    # number  is a jinja var in the HTML template
    return render_template("score.html", number=score)

## in the HTML file in ./templates
## insert a variable: {{ var }}
## insert a python logic: {% if a>b  %}
## HTML does not have indentation, use {% endif %} to end

if __name__=="__main__":
    app.run(host='0.0.0.0', port=2224)
