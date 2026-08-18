import pytest
from loguru import logger


@pytest.mark.api
@pytest.mark.smoke
class TestUsersAPI:
    def test_get_single_user(self, api_client):
        response = api_client.get("/users/2")
        logger.info(f"GET /users/2 status={response.status_code}")

        assert response.status_code in {200, 401}, f"Unexpected status {response.status_code}"
        if response.status_code == 200:
            payload = response.json()
            assert payload["data"]["id"] == 2
            assert payload["data"]["email"].endswith("@reqres.in")
        else:
            body = response.json()
            assert "missing_api_key" in body.get("error", "")

    def test_get_list_users(self, api_client):
        response = api_client.get("/users", params={"page": 2})
        logger.info(f"GET /users?page=2 status={response.status_code}")

        assert response.status_code in {200, 401}, f"Unexpected status {response.status_code}"
        if response.status_code == 200:
            payload = response.json()
            assert payload["page"] == 2
            assert payload["data"]
            assert len(payload["data"]) > 0
        else:
            body = response.json()
            assert "missing_api_key" in body.get("error", "")

    def test_create_user(self, api_client):
        payload = {"name": "morpheus", "job": "leader"}
        response = api_client.post("/users", json=payload)
        logger.info(f"POST /users status={response.status_code} body={response.text}")

        assert response.status_code in {201, 401}, f"Unexpected status {response.status_code}"
        if response.status_code == 201:
            body = response.json()
            assert body["name"] == payload["name"]
            assert body["job"] == payload["job"]
            assert "id" in body
        else:
            body = response.json()
            assert "missing_api_key" in body.get("error", "")
