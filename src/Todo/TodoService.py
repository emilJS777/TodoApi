
from ..__Parents.Repository import Repository
from .ITodoRepo import ITodoRepo
from ..__Parents.Service import Service


class TodoService(Service, Repository):
    def __init__(self, todo_repository: ITodoRepo):
        self.todo_repository: ITodoRepo = todo_repository

    def create(self, body: dict) -> dict:
        self.todo_repository.create(body=body)
        return self.response_created()

    def update(self, todo_id: int, body: dict) -> dict:
        todo = self.todo_repository.get_by_id(todo_id)
        if not todo:
            return self.response_not_found('todo not found')
        self.todo_repository.update(todo=todo, body=body)
        return self.response_updated('todo updated')

    def on_completed(self, todo_id: int) -> dict:
        todo = self.todo_repository.get_by_id(todo_id)
        if not todo:
            return self.response_not_found('todo not found')
        self.todo_repository.on_completed(todo)
        return self.response_updated()

    def delete(self, todo_id: int) -> dict:
        todo = self.todo_repository.get_by_id(todo_id)
        if not todo:
            return self.response_not_found('todo not found')
        self.todo_repository.delete(todo)
        return self.response_deleted('todo deleted')

    def get_by_id(self, todo_id: int) -> dict:
        todo = self.todo_repository.get_by_id(todo_id)
        if not todo:
            return self.response_not_found('todo not found')
        return self.response_ok({
            "id": todo.id,
            "title": todo.title,
            "description": todo.description,
            "creation_date": todo.creation_date,
            "priority": todo.priority,
            "completed": todo.completed
        })

    def get_all(self, page: int, per_page: int, completed: bool or None, priority: int or None) -> dict:
        todos: list = self.todo_repository.get_all(page=page, per_page=per_page, completed=completed, priority=priority)
        return self.response_ok([{
            "id": todo.id,
            "title": todo.title,
            "description": todo.description,
            "creation_date": todo.creation_date,
            "priority": todo.priority,
            "completed": todo.completed
        } for todo in todos])
        