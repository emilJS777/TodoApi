from .IUserRepo import IUserRepo
from .UserModel import User
from flask_bcrypt import generate_password_hash


class UserRepository(IUserRepo):
    user: User = User

    def create(self, body: dict) -> User:
        user = self.user()
        user.name = body['name']
        user.password_hash = generate_password_hash(body['password'])
        user.first_name = body['first_name'].title()
        user.last_name = body['last_name'].title()
        user.save_db()
        return user

    def update(self, user_id: int, body: dict):
        user = self.user.query.filter_by(id=user_id).first()

        if body.get('name'):
            user.name = body['name']

        if body.get('first_name'):
            user.first_name = body['first_name']

        if body.get('last_name'):
            user.last_name = body['last_name']

        user.update_db()
        return user

    def delete(self, user_id: int):
        user = self.user.query.filter_by(id=user_id).first()
        user.delete_db()
        return user

    def get_by_id(self, user_id: int) -> User:
        user = self.user.query.filter_by(id=user_id).first()
        return user

    def get_by_name(self, name: str) -> User:
        user = self.user.query.filter_by(name=name).first()
        return user

    def get_by_name_exclude_id(self, user_id: int, name: str):
        user = self.user.query.filter(self.user.id != user_id, self.user.name == name).first()
        return user
