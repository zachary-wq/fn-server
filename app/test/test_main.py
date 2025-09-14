from http.client import responses

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/api/v1/health/home")
    assert response.status_code == 200
    assert response.text == "success"

