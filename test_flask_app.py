"""
This module will conduct test for Flask APIs
"""

# import flask app object from python file containing it
from flask_app import app
import json
import pytest

@pytest.fixture # <-- Hardcoded, do not change
def client():
    return app.test_client() # <-- Hardcoded, do not change

def test_home(client):
    response=client.get('/')
    assert response.status_code == 200

def test_contact(client):
    response=client.get('/contact_us')
    assert response.status_code == 200

def test_greet(client):
    response = client.post('/greet', json={'name':'Ankit'})
    assert response.status_code == 200
    assert response.get_json() == {'Greetings':'Hello Ankit'}