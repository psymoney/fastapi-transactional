from dependency_injector import providers
from dependency_injector.containers import DeclarativeContainer, \
    WiringConfiguration

from app.database import get_session
from app.domain.repository import Repository
from app.domain.service import AService


class Container(DeclarativeContainer):
    wiring_config = WiringConfiguration(
        modules=[
            '.domain.endpoint',
        ],
    )

    session_factory = providers.Callable(get_session)

    repository = providers.Factory(
        Repository,
        session_factory=session_factory
    )

    service = providers.Factory(
        AService,
        repository=repository
    )
