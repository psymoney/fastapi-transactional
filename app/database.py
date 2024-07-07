from asyncio import current_task
from contextlib import AbstractContextManager, asynccontextmanager
from typing import Callable

from sqlalchemy.ext.asyncio import create_async_engine, async_scoped_session, \
    async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Database:
    def __init__(self):
        url = ''
        self._engine = create_async_engine(url)

        self._session_maker = async_sessionmaker(
            bind=self._engine,
            autoflush=False,
            autocommit=False
        )

        self._session_factory = async_scoped_session(
            self._session_maker,
            scopefunc=current_task
        )

    def create_database(self):
        Base.metadata.create_all(self._engine)

    @asynccontextmanager
    async def session(self) -> Callable[..., AbstractContextManager[AsyncSession]]:
        session = self._session_factory()
        try:
            yield session
        except Exception as e:
            await session.rollback()
            raise e
        finally:
            await session.close()

