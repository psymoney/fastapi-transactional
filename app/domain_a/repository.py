from contextlib import AbstractAsyncContextManager
from typing import Callable

from sqlalchemy.ext.asyncio import AsyncSession


class ARepository:
    def __init__(
            self,
            session_factory: Callable[..., AbstractAsyncContextManager[AsyncSession]]
    ):
        self._session = session_factory

    async def do_first(self):
        async with self._session() as db:
            print(db)

    async def do_second(self):
        async with self._session() as db:
            print(db)

    async def do_third(self):
        async with self._session() as db:
            print(db)
