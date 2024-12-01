"""
This is basic code showcasing Flask API
Same will be tested using pytest
"""
from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to Flask API testing using pytest"

@app.route("/contact_us")
def contact():
    return {'Phone Number': 1234567890,
            'email':'testing@flask.api'}
