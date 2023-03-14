"""Application module."""

from fastapi import FastAPI

from .containers import Container
from . import endpoints


def create_app() -> FastAPI:
    container = Container()
    db = container.db()
    db.create_database()
    app1 = FastAPI()
    app1.container = container
    app1.include_router(endpoints.router)
    return app1


app = create_app()
