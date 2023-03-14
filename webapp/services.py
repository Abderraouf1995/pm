from uuid import uuid4
from typing import Iterator

from .repositories import UserRepository, ProjectRepository
from .models import User, Project


class UserService:

    def __init__(self, user_repository: UserRepository) -> None:
        self._repository: UserRepository = user_repository

    def get_users(self) -> Iterator[User]:
        return self._repository.get_all()

    def get_user_by_id(self, user_id: int) -> User:
        return self._repository.get_by_id(user_id)

    def create_user(self) -> User:
        uid = uuid4()
        return self._repository.add(email=f"{uid}@email.com", password="pwd1")

    def delete_user_by_id(self, user_id: int) -> None:
        return self._repository.delete_by_id(user_id)


class ProjectService:

    def __init__(self, project_repository: ProjectRepository) -> None:
        self._repository: ProjectRepository = project_repository

    def get_users(self) -> Iterator[Project]:
        return self._repository.get_all()

    def get_user_by_id(self, project_id: int) -> Project:
        return self._repository.get_by_id(project_id)

    def create_user(self) -> Project:
        uid = uuid4()
        return self._repository.add(task=f"{uid}@email.com", project="pwd1")

    def delete_user_by_id(self, project_id: int) -> None:
        return self._repository.delete_by_id(project_id)


