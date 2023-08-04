from src import db
from src.__Parents.Model import Model


class User(Model, db.Model):
    name = db.Column(db.String(60), nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    first_name = db.Column(db.String(60), nullable=False)
    last_name = db.Column(db.String(60), nullable=False)