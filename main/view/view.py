from main import app
from flask import render_template, request, send_file, Flask, make_response

@app.route('/')
def index():
    return '<h1>sex knowledge web<h1>'
