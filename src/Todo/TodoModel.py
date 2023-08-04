from src import db
from src.__Parents.Model import Model
from sqlalchemy import func


class Todo(db.Model, Model):
	title = db.Column(db.String(120), nullable=False)
	description = db.Column(db.String(2000))
	priority = db.Column(db.Integer, default=0)
	creation_date = db.Column(db.DateTime(timezone=True), default=func.now())
	user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
	completed = db.Column(db.Boolean, default=False)
