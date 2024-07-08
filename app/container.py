from dependency_injector import providers
from dependency_injector.containers import DeclarativeContainer, \
    WiringConfiguration

from app.database import Database
from app.domain_a.repository import ARepository
from app.domain_a.service import AService


class Container(DeclarativeContainer):
    wiring_config = WiringConfiguration(
        modules=[
            '.domain_a.endpoint',
            '.domain_a.service'
        ],
    )

    db = providers.Singleton(Database)

    transactional = providers.Callable(session=db.provided.session)

    a_repository = providers.Factory(
        ARepository,
        session_factory=db.provided.session
    )

    a_service = providers.Factory(
        AService,
        repository=a_repository,
        session_factory=db.provided.session
    )
