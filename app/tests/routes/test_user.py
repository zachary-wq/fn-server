
from ..conftest import get_client

class TestUser:

    def test_wrong_password(self):
        client = get_client()
        response = client.get("/api/v1/users/me")
        assert response.status_code == 401
        # assert response.text == "success"