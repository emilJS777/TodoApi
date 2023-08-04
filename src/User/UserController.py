from src.User.UserService import UserService
from src.User.UserRepository import UserRepository
from src.__Parents.Controller import Controller
from flask_expects_json import expects_json
from src.User.UserValidator import user_schema


class UserController(Controller):
    user_service: UserService = UserService(UserRepository())

    @expects_json(user_schema)
    def post(self) -> dict:
        res: dict = self.user_service.create(body=self.request.get_json())
        return res
