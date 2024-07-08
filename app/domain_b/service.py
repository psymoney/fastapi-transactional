import asyncio

from .repository import BRepository
from ..database import transactional


class BService:
    def __init__(
            self,
            repository: BRepository
    ):
        self._repository = repository

    @transactional
    async def transactional_service(self):
        keys = {}

        print('i sleep')
        await asyncio.sleep(3)
        keys['1st'] = await self._repository.do_first()
        keys['2nd'] = await self._repository.do_second()
        keys['3rd'] = await self._repository.do_third()

        return keys
