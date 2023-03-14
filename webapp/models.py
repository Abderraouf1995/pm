from sqlalchemy import Column, String, Boolean, Integer

from .database import Base


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    def __repr__(self):
        return f"<User(id={self.id}, " \
               f"email=\"{self.email}\", " \
               f"hashed_password=\"{self.hashed_password}\", " \
               f"is_active={self.is_active})>"


class Project (Base):

    __tablename__ = "projects"

    id = Column(Integer, primary_key=True)
    task = Column(String, unique=True)
    project = Column(String)
    deadline = Column(Boolean, default=True)

    def __repr__(self):
        return f"<Project(id={self.id}, " \
               f"tasks=\"{self.task}\", " \
               f"project=\"{self.project}\", " \
               f"deadline={self.deadline})>"


class Adm (Base):

    __tablename__ = "adm"

    id = Column(Integer, primary_key=True)
    task = Column(String, unique=True)
    project = Column(String)
    deadline = Column(Boolean, default=True)

    def __repr__(self):
        return f"<Project(id={self.id}, " \
               f"tasks=\"{self.task}\", " \
               f"project=\"{self.project}\", " \
               f"deadline={self.deadline})>"

