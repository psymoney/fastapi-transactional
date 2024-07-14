import asyncio

import httpx
import pytest
from fastapi.testclient import TestClient

from app.application import app


@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c


@pytest.mark.asyncio
async def test_transactional(client):
    async with httpx.AsyncClient(app=client, base_url="http://localhost") as async_client:
        requests = [
            async_client.get("/")
            for i in range(10)
        ]
        responses = await asyncio.gather(*requests)

        for response in responses:
            print(response)

