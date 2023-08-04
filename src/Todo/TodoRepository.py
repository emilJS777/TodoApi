from .ITodoRepo import ITodoRepo
from .TodoModel import Todo
from flask import g


class TodoRepository(ITodoRepo):
    def create(self, body: dict):
        todo: Todo = Todo()
        todo.title = body['title']
        todo.description = body['description']
        todo.priority = body['priority']
        todo.user_id = g.user_id
        todo.save_db()

    def update(self, todo: Todo, body: dict):
        todo.title = body['title']
        todo.description = body['description']
        todo.priority = body['priority']
        todo.update_db()

    def on_completed(self, todo: Todo):
        todo.completed = False if todo.completed else True
        todo.update_db()
        
    def delete(self, todo: Todo):
        todo.delete_db()

    def get_by_id(self, todo_id: int) -> Todo:
        todo: Todo = Todo.query.filter_by(id=todo_id, user_id=g.user_id).first()
        return todo

    def get_all(self, page: int, per_page: int, completed: bool or None, priority: int or None):
        todos = Todo.query.filter_by(user_id=g.user_id)\
            .filter(Todo.completed == completed if completed != None else Todo.id.isnot(None)) \
            .filter(Todo.priority == priority if priority != None else Todo.id.isnot(None)) \
            .order_by(-Todo.creation_date)\
            .paginate(page=page, per_page=per_page)
        return todos
