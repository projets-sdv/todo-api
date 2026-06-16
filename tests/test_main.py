from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_get_todos():
    response = client.get("/todos")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_todo():
    response = client.post("/todos", json={"title": "test todo"})
    assert response.status_code == 200
    assert response.json()["title"] == "test todo"

def test_delete_todo():
    create_response = client.post("/todos", json={"title": "todo to delete"})
    todo_id = create_response.json()["id"]

    delete_response = client.delete(f"/todos/{todo_id}")
    assert delete_response.status_code == 200
    assert delete_response.json()["message"] == "Todo deleted"
