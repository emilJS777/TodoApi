from sqlalchemy.orm import relationship
from src import db
from src.__Parents.Model import Model


class Auth(Model, db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = relationship("User")
    access_token = db.Column(db.String(520), nullable=False)

    def __init__(self, user_id: int):
        self.user_id = user_id
        