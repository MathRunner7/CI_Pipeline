"""
This is basic code showcasing Flask API
Same will be tested using pytest
"""
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to Flask API testing using pytest"

@app.route("/contact_us")
def contact():
    return {'Phone Number': 1234567890,
            'email':'testing@flask.api'}

@app.route("/greet", methods=['GET','POST'])
def greet():
    if request.method=='GET':
        return "What is your name?"
    if request.method=='POST':
        name = request.get_json()['name']
        answer = f"Hello {name}"
        return jsonify({'Greetings':answer})
