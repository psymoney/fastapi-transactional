from asyncio import current_task
from contextlib import AbstractAsyncContextManager
from typing import Callable

from sqlalchemy.ext.asyncio import AsyncSession


class Repository:
    def __init__(
            self,
            session_factory: Callable[..., AbstractAsyncContextManager[AsyncSession]]
    ):
        self._session = session_factory

    async def do_first(self):
        async with self._session() as db:
            print(f'1st repo task: {current_task()}')
            print(f'1st repo: {id(db)}')
            return id(db)

    async def do_second(self):
        async with self._session() as db:
            print(f'2nd repo task: {current_task()}')

            print(f'2nd repo: {id(db)}')
            return id(db)

    async def do_third(self):
        async with self._session() as db:
            print(f'3rd repo task: {current_task()}')

            print(f'3rd repo: {id(db)}')
            return id(db)
