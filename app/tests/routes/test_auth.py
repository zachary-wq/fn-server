
from ..conftest import get_client

class TestAuth:

    def test_un_auth_api(self):
        pass

    def test_wrong_password(self):
        client = get_client()
        response = client.post("/api/v1/auth/login/access-token", data={
            "username": "test@email",
            "password": "test"
        })
        assert response.status_code == 400
        # assert response.text == "success"