import functools
from typing import Callable, Any

from dependency_injector.wiring import Provide

from app.container import Container


def transactional(
        function: Callable[..., Any],
        provider=Provide[Container.db]
) -> Callable[..., Any]:
    print(f'provider = {provider}')
    # print(provider.session)
    @functools.wraps(function)
    async def decorator(*args, **kwargs):
        from app.container import Container

        print(provider.__dict__)
        db = provider[Container.db]
        print(db)

        print(args)
        print(kwargs)

        async with db.session() as transaction:
            print(transaction)
            return await function(*args, **kwargs)

    return decorator
