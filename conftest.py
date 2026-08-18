import pytest
from core.config_manager import ConfigManager
from core.browser_manager import BrowserManager
from core.api_client import APIClient
from utilities.logger import setup_logger
from utilities.logger import setup_logger

# Initialize logger once for the whole test run
logger = setup_logger()

# Initialize logger once for the whole test run
# setup_logger()

@pytest.fixture(scope="session", autouse=True)
def load_config():
    """
    Load configuration once per test session.
    """
    config = ConfigManager.load_config()
    return config


@pytest.fixture(scope="function")
def browser(load_config):
    """
    Provide a browser driver (Selenium or Playwright) based on config.
    """
    driver = BrowserManager().get_driver()
    yield driver
    # Teardown
    if load_config.get("driver") == "selenium":
        driver.quit()
    else:
        driver.close()


@pytest.fixture(scope="function")
def api_client(load_config):
    """
    Provide a reusable API client for tests.
    """
    base_url = load_config["api"]["base_url"]
    token = load_config["api"].get("token")
    client = APIClient(base_url=base_url, token=token)
    yield client
    client.client.close()


@pytest.fixture(scope="function")
def hybrid_client(browser, api_client):
    """
    Combine browser + API client for hybrid tests.
    """
    yield {"browser": browser, "api": api_client}


# https://copilot.microsoft.com/chats/hSpbw55sA7yS3KLrGtW3j