from dependency_injector import providers
from dependency_injector.containers import DeclarativeContainer, \
    WiringConfiguration

from app.database import Database, get_session
from app.domain_a.repository import ARepository
from app.domain_a.service import AService
from app.domain_b.repository import BRepository
from app.domain_b.service import BService


class Container(DeclarativeContainer):
    wiring_config = WiringConfiguration(
        modules=[
            '.domain_a.endpoint',
            '.domain_b.endpoint',
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


class ContainerB(DeclarativeContainer):
    wiring_config = WiringConfiguration(
        modules=[
            '.domain_a.endpoint',
            '.domain_b.endpoint',
        ],
    )

    db = providers.Callable(get_session)

    a_repository = providers.Factory(
        ARepository,
        session_factory=db
    )

    a_service = providers.Factory(
        AService,
        repository=a_repository,
        session_factory=db.provided.session
    )

    b_repository = providers.Factory(
        BRepository,
        session=db
    )

    b_service = providers.Factory(
        BService,
        repository=b_repository
    )

