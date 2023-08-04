from src.Auth.IAuthRepo import IAuthRepo
from src.__Parents.Repository import Repository
from .AuthModel import Auth
from src import app
import jwt


class AuthRepository(Repository, IAuthRepo):

    def generate_tokens(self, user_id: int):
        auth: Auth = Auth.query.filter_by(user_id=user_id).first() or Auth(user_id)
        auth.access_token = jwt.encode({'user_id': user_id}, app.config['JWT_SECRET_KEY'], app.config['JWT_ALGORITHM'])
        auth.update_db() or auth.save_db()
        return {'access_token': auth.access_token}

    def delete_by_user_id(self, user_id: int):
        Auth.query.filter_by(user_id=user_id).delete()

    def get_by_user_id(self, user_id: int):
        auth: Auth = Auth.query.filter_by(user_id=user_id).first()
        return auth