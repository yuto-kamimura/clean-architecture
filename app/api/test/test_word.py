from fastapi.testclient import TestClient
from app.api.routes.word import router

client = TestClient(router)

def test_create_word_endpoint():
    # Test case for creating a word
    word_data = {"word": "example"}
    response = client.post("/words/", json=word_data)
    assert response.status_code == 200
    assert response.json() == {"message": "Word created successfully"}

def test_get_word_endpoint():
    # Test case for getting a word by ID
    word_id = 1
    response = client.get(f"/words/{word_id}")
    assert response.status_code == 200
    assert response.json() == {"id": word_id, "word": "example"}
