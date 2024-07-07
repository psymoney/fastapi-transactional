from typing import Callable

from app.domain_a.repository import ARepository


class AService:
    def __init__(self, repository: ARepository, deco: Callable):
        self._repository = repository
        self.transactional_service = deco(self.transactional_service)

    async def transactional_service(self):
        await self._repository.do_first()
        await self._repository.do_second()
        await self._repository.do_third()

        return 'yes'
