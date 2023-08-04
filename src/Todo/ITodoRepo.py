
from abc import ABC, abstractmethod
from .TodoModel import Todo


class ITodoRepo(ABC):
    @abstractmethod
    def create(self, body: dict):
        pass

    @abstractmethod
    def update(self, todo: Todo, body: dict):
        pass

    @abstractmethod
    def delete(self, todo: Todo):
        pass

    @abstractmethod
    def on_completed(self, todo: Todo):
        pass

    @abstractmethod
    def get_by_id(self, todo_id: int) -> Todo:
        pass

    @abstractmethod
    def get_all(self, page: int, per_page: int, completed: bool or None, priority: int or None):
        pass
        