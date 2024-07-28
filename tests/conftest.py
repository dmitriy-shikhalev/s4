import pytest
from fastapi.testclient import TestClient

from s4.connection import get_session
from s4.router import app as router_app


@pytest.fixture
def session():
    with get_session() as session_:
        try:
            yield session_
        finally:
            session_.rollback()


@pytest.fixture
def test_client_router():
    yield TestClient(router_app)
