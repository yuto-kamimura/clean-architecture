from fastapi.testclient import TestClient
from app.main import app
from app.interfaces.usecases.user_usecase import UserUseCases
from app.core.schemas.user import User

client = TestClient(app)

class MockUserUseCases(UserUseCases):
    def __init__(self):
        pass

    def create_user(self, user) -> User:
        test_user = {"id": 1, "name": user.name, "password": user.password, "email": user.email}
        return test_user

    def get_user(self, user_id) -> User:
        test_user = {"id": 1, "name": "test", "email": "test@test.com"}
        return test_user

    def authenticate_user(self, plain_user) -> User:
        test_user = {"id": 1, "name": "test", "email": "test@test.com"}
        return test_user
    
def test_create_user_endpoint():
    response = client.post("/users/", json={"name": "test", "email": "test@test.com", "password": "test"})
    assert response.status_code == 201
    assert "id" in response.json()
    assert response.json()["name"] == "test"
    assert response.json()["email"] == "test@test.com"

def test_create_user_endpoint_with_invalid_data():
    response = client.post("/users/", json={"name": "", "email": "test@test.com", "password": "test"})
    assert response.status_code == 400

def test_get_user_endpoint():
    response = client.post("/users/", json={"name": "test", "email": "test@test.com", "password": "test"})
    user_id = response.json()["id"]
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["id"] == user_id
    assert response.json()["name"] == "test"
    assert response.json()["email"] == "test@test.com"

def test_get_user_endpoint_with_invalid_id():
    response = client.get("/users/9999")
    assert response.status_code == 404

def test_post_user_endpoint():
    response = client.post("/users/", json={"name": "test", "email": "test@test.com", "password": "test"})
    response = client.post("/login/", json={"email": "test@test.com", "password": "test"})
    assert response.status_code == 200
    assert response.json()["email"] == "test@test.com"

def test_post_user_endpoint_with_invalid_data():
    response = client.post("/login/", json={"email": "test@test.com", "password": "wrong_password"})
    assert response.status_code == 403