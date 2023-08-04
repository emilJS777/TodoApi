from abc import ABC, abstractmethod


class IUserRepo(ABC):

    @abstractmethod
    def create(self, body: dict) -> dict:
        pass

    @abstractmethod
    def update(self, user_id: int, body: dict):
        pass

    @abstractmethod
    def delete(self, user_id: int):
        pass

    @abstractmethod
    def get_by_id(self, user_id: int):
        pass

    @abstractmethod
    def get_by_name(self, name: str):
        pass

    @abstractmethod
    def get_by_name_exclude_id(self, user_id: int, name: str):
        pass