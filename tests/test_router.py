from fastapi.testclient import TestClient


def test_ping(test_client_router: TestClient):
    response = test_client_router.get("/ping")

    assert response.status_code == 200
    assert response.text == '"pong"'
