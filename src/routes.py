from . import api
from .Todo.TodoController import TodoController
from .User.UserController import UserController
from .Auth.AuthController import AuthController

api.add_resource(TodoController, "/todo")
api.add_resource(UserController, "/user")
api.add_resource(AuthController, "/auth")
