from {{cookiecutter.application_name}} import db

class User(db.model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))