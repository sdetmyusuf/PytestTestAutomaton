import httpx
from loguru import logger


class APIClient:
    def __init__(self, base_url: str, token: str = None, api_key: str = None):
        self.base_url = base_url
        self.client = httpx.Client(base_url=base_url, timeout=10)
        if token:
            self.client.headers.update({"Authorization": f"Bearer {token}"})
        if api_key:
            self.client.headers.update({"x-api-key": api_key})

    def get(self, endpoint: str, **kwargs):
        logger.info(f"GET {endpoint}")
        return self.client.get(endpoint, **kwargs)

    def post(self, endpoint: str, json=None, **kwargs):
        logger.info(f"POST {endpoint} {json}")
        return self.client.post(endpoint, json=json, **kwargs)