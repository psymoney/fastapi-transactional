from functools import wraps
from asyncio import current_task
from typing import Callable, Awaitable

from sqlalchemy.ext.asyncio import create_async_engine, async_scoped_session, \
    async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base


Base = declarative_base()

url = 'mysql+aiomysql://username:password@localhost/test?charset=utf8mb4'

_engine = create_async_engine(url)

_async_session_factory = async_scoped_session(
    async_sessionmaker(
        bind=_engine,
        autoflush=False,
        autocommit=False
    ),
    scopefunc=current_task
)


def get_session():
    return _async_session_factory()


def session() -> AsyncSession:
    return _async_session_factory()


AsyncCallable = Callable[..., Awaitable]


def transactional(function):

    @wraps(function)
    async def decorator(*args, **kwargs):
        try:
            asession: AsyncSession = session()

            if asession.in_transaction():
                return await function(*args, **kwargs)

            async with asession.begin():
                result = await function(*args, **kwargs)

            return result

        except Exception as e:
            raise

    return decorator
