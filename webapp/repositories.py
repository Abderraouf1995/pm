from contextlib import AbstractContextManager
from typing import Callable, Iterator

from sqlalchemy.orm import Session

from .models import User
from .models import Project


class UserRepository:

    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]) -> None:
        self.session_factory = session_factory

    def get_all(self) -> Iterator[User]:
        with self.session_factory() as session:
            return session.query(User).all()

    def get_by_id(self, user_id: int) -> User:
        with self.session_factory() as session:
            user = session.query(User).filter(User.id == user_id).first()
            if not user:
                raise UserNotFoundError(user_id)
            return user

    def add(self, email: str, password: str, is_active: bool = True) -> User:
        with self.session_factory() as session:
            user = User(email=email, hashed_password=password, is_active=is_active)
            session.add(user)
            session.commit()
            session.refresh(user)
            return user

    def delete_by_id(self, user_id: int) -> None:
        with self.session_factory() as session:
            entity: User = session.query(User).filter(User.id == user_id).first()
            if not entity:
                raise UserNotFoundError(user_id)
            session.delete(entity)
            session.commit()


class ProjectRepository:

    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]) -> None:
        self.session_factory = session_factory

    def get_all(self) -> Iterator[Project]:
        with self.session_factory() as session:
            return session.query(Project).all()

    def get_by_id(self, project_id: int) -> Project:
        with self.session_factory() as session:
            user = session.query(Project).filter(Project.id == project_id).first()
            if not user:
                raise UserNotFoundError(project_id)
            return user

    def add(self, project: str, task: str, deadline: bool = True) -> Project:
        with self.session_factory() as session:
            user = Project(project=project, task=task, deadline=deadline)
            session.add(user)
            session.commit()
            session.refresh(user)
            return user

    def delete_by_id(self, project_id: int) -> None:
        with self.session_factory() as session:
            entity: Project = session.query(Project).filter(Project.id == project_id).first()
            if not entity:
                raise UserNotFoundError(project_id)
            session.delete(entity)
            session.commit()


class NotFoundError(Exception):

    entity_name: str

    def __init__(self, entity_id):
        super().__init__(f"{self.entity_name} not found, id: {entity_id}")


class UserNotFoundError(NotFoundError):

    entity_name: str = "User"


class ProjectNotFoundError(NotFoundError):

    entity_name: str = "Project"
