from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_register_login_flow():
    payload = {"name": "Test User", "email": "test@example.com", "password": "password123", "role": "candidate"}
    register = client.post("/api/auth/register", json=payload)
    assert register.status_code == 200
    token = register.json()["access_token"]
    assert token

    login = client.post("/api/auth/login", json={"email": "test@example.com", "password": "password123"})
    assert login.status_code == 200
    assert "access_token" in login.json()
