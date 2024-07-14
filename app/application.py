from fastapi import FastAPI

from app.container import Container
from .domain.endpoint import router


def get_app():
    container = Container()

    app = FastAPI()
    app.container = container

    app.include_router(router)

    return app


app = get_app()
