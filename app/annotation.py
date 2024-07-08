import functools
from typing import Callable

#
# def transactional(function: Callable) -> Callable:
#
#     @functools.wraps(function)
#     async def decorator(*args, **kwargs):
#         from app.container import Container
#
#         print(provider.__dict__)
#         db = provider[Container.db]
#         print(db)
#
#         print(args)
#         print(kwargs)
#
#         async with db.session() as transaction:
#             print(transaction)
#             return await function(*args, **kwargs)
#
#     return decorator
