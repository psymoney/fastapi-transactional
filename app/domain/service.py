import asyncio
from asyncio import current_task

from app.database import transactional
from app.domain.repository import Repository


class AService:
    def __init__(
            self,
            repository: Repository
    ):
        self._repository = repository

    @transactional
    async def transactional_service(self):
        print(current_task())
        keys = {}
        await asyncio.sleep(1)
        keys['1st'] = await self._repository.do_first()
        keys['2nd'] = await self._repository.do_second()
        keys['3rd'] = await self._repository.do_third()

        return keys
