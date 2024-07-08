import asyncio
from contextlib import AbstractAsyncContextManager
from typing import Callable

from sqlalchemy.ext.asyncio import AsyncSession

from app.domain_a.repository import ARepository


class AService:
    def __init__(
            self,
            repository: ARepository,
            session_factory: Callable[..., AbstractAsyncContextManager[AsyncSession]]
    ):
        self._repository = repository
        self._session_factory = session_factory

    async def transactional_service(self):
        keys = {}
        async with self._session_factory() as db:
            print(f'service: {id(db)}')
            print('i sleep')
            await asyncio.sleep(3)
            keys['ser'] = id(db)
            keys['1st'] = await self._repository.do_first()
            keys['2nd'] = await self._repository.do_second()
            keys['3rd'] = await self._repository.do_third()

        return keys
