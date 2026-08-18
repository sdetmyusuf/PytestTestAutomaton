import pytest
from core.browser_manager import BrowserManager
from core.api_client import APIClient
from core.config_manager import ConfigManager

@pytest.fixture(scope="function")
def hybrid_client():
    config = ConfigManager.load_config()
    browser = BrowserManager().get_driver()
    api = APIClient(base_url=config["api"]["base_url"], token=config["api"].get("token"))
    yield {"browser": browser, "api": api}
    if config.get("driver") == "selenium":
        browser.quit()
