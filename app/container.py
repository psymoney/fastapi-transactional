from dependency_injector import providers
from dependency_injector.containers import DeclarativeContainer, \
    WiringConfiguration

from app.database import Database
from app.domain_a.repository import ARepository
from app.domain_a.service import AService


class Container(DeclarativeContainer):
    wiring_config = WiringConfiguration(modules=[
        '.domain_a.endpoint'
    ])

    db = providers.Singleton(Database)

    a_repository = providers.Factory(
        ARepository,
        sesseion_factory=db.provided.session
    )

    a_service = providers.Factory(
        AService,
        repository=a_repository
    )
