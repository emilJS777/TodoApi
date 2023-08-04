from .IUserRepo import IUserRepo
from flask import g
from ..__Parents.Repository import Repository
from ..__Parents.Service import Service


class UserService(Service, Repository):

    def __init__(self, user_repository: IUserRepo):
        self._user_repository: IUserRepo = user_repository

    # CREATE
    def create(self, body: dict) -> dict:
        if self._user_repository.get_by_name(body['name']):
            return self.response_conflict("username exist")
        self._user_repository.create(body)
        return self.response_created()


