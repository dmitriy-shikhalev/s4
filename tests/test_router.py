from fastapi.testclient import TestClient

from s4.router import app


def test_ping():
    response = TestClient(app)
