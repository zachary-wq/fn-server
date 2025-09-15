from .base import client

class TestAuth:

    def test_un_auth_api(self):
        pass

    def test_wrong_password(self):
        response = client.post("/api/v1/auth/login/access-token", data={
            "username": "test@email",
            "password": "test"
        })
        assert response.status_code == 422
        assert response.text == "success"