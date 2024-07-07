import pytest
from fastapi.testclient import TestClient

from app.application import app


@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c


def test_transactional(client):
    res = client.get('/domain-a')
    print(res)
