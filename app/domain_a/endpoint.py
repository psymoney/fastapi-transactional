from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends

from app.container import Container
from app.domain_a.service import AService

router = APIRouter()


@router.get('/domain-a')
@inject
async def domain_a(a_service: AService = Depends(Provide[Container.a_service])):
    pass
