from http.client import responses
from .base import client


def test_health():
    response = client.get("/api/v1/health/home")
    assert response.status_code == 200
    assert response.text == "success"

