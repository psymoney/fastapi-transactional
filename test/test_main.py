import threading
from time import sleep

import pytest
from fastapi.testclient import TestClient

from app.application import app


@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c

@pytest.fixture
def client_2():
    with TestClient(app) as c:
        yield c


def test_transactional(client, client_2):
    t1 = threading.Thread(target=client.get('/domain-a').json())
    t2 = threading.Thread(target=client_2.get('/domain-a').json())

    t1.start()
    t2.start()

    sleep(10)
