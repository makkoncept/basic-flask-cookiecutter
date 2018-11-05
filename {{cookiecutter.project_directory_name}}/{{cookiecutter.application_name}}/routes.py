from {{cookiecutter.application_name}} import app, db
from flask import render_template, make_response, jsonify, request

@app.route('/')
def index():
    return render_template('index.html')