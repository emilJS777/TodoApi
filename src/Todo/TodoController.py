from .TodoService import TodoService
from .TodoRepository import TodoRepository
from ..__Parents.Controller import Controller
from src.Auth.AuthMiddleware import AuthMiddleware
from flask_expects_json import expects_json
from .TodoValidator import todo_schema


class TodoController(Controller):
    todo_service: TodoService = TodoService(TodoRepository())

    @expects_json(todo_schema)
    @AuthMiddleware.check_authorize
    def post(self) -> dict:
        res: dict = self.todo_service.create(body=self.request.get_json())
        return res

    @expects_json(todo_schema)
    @AuthMiddleware.check_authorize
    def put(self) -> dict:
        res: dict = self.todo_service.update(todo_id=self.id, body=self.request.get_json())
        return res

    @AuthMiddleware.check_authorize
    def patch(self) -> dict:
        res: dict = self.todo_service.on_completed(todo_id=self.id)
        return res

    @AuthMiddleware.check_authorize
    def delete(self) -> dict:
        res: dict = self.todo_service.delete(todo_id=self.id)
        return res

    @AuthMiddleware.check_authorize
    def get(self) -> dict:
        if self.id:
            res: dict = self.todo_service.get_by_id(self.id)
        else:
            if self.arguments.get('completed') == '':
                completed = None
            else:
                completed = self.arguments.get('completed').lower() == 'true'

            if self.arguments.get('priority') == '':
                priority = None
            else:
                priority = int(self.arguments.get('priority'))

            res: dict = self.todo_service.get_all(
                page=self.page,
                per_page=self.per_page,
                completed=completed,
                priority=priority)
        return res
        