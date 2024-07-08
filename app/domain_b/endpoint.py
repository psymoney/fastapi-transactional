from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends

from .service import BService
from ..container import ContainerB

router = APIRouter()


@router.get('/domain-a')
@inject
async def domain_a(b_service: BService = Depends(Provide[ContainerB.b_service])):
    res = await b_service.transactional_service()
    print(res)
    return res


@router.get('/domain-b')
@inject
async def domain_a(b_service: BService = Depends(Provide[ContainerB.b_service])):
    res = await b_service.transactional_service()
    print(res)
    return res
