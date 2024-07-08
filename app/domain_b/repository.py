from sqlalchemy.ext.asyncio import AsyncSession


class BRepository:
    def __init__(
            self,
            session: AsyncSession
    ):
        self._session = session

    async def do_first(self):
        print(f'1st repo: {id(self._session)}')
        return id(self._session)

    async def do_second(self):
        print(f'2nd repo: {id(self._session)}')
        return id(self._session)

    async def do_third(self):
        print(f'3rd repo: {id(self._session)}')
        return id(self._session)
