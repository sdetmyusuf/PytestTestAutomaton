import pytest


@pytest.fixture(scope="function")
def api_client(load_config):
    from core.api_client import APIClient

    base_url = load_config["api"]["base_url"]
    token = load_config["api"].get("token")
    api_key = load_config["api"].get("api_key")
    client = APIClient(base_url=base_url, token=token, api_key=api_key)
    yield client
    client.client.close()
