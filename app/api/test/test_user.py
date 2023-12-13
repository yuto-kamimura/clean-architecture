from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_user_endpoint():
    response = client.get("/users/")
    assert response.status_code == 201
