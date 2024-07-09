import asyncio
import time

from fastapi import FastAPI

from app.container import Container, ContainerB
from .domain_a.endpoint import router as a_router
from .domain_b.endpoint import router as b_router


def get_app_a():
    container = Container()
    db = container.db()
    # db.create_database()

    app = FastAPI()
    app.container = container

    app.include_router(a_router, prefix='/a')
    app.include_router(b_router, prefix='/b')

    return app


def get_app_b():
    container = ContainerB()

    app = FastAPI()
    app.container = container

    app.include_router(a_router, prefix='/a')
    app.include_router(b_router, prefix='/b')

    return app


# app = get_app_b()

app = FastAPI()

@app.get('/dd')
async def dd():
    s = time.perf_counter()
    print('got it will proceed computing')
    await asyncio.sleep(2)
    e = time.perf_counter() - s
    print(f'time spent: {e}, handled at {time.time()}')
    return "OK"
