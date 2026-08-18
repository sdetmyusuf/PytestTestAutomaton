from core.config_manager import ConfigManager


class BrowserManager:
    def __init__(self):
        self.config = ConfigManager.load_config()

    def get_driver(self):
        if self.config.get("driver") == "selenium":
            try:
                from selenium import webdriver
            except ImportError as exc:
                raise ImportError("Selenium is not installed. Install it with 'pip install selenium'.") from exc
            return webdriver.Chrome()
        elif self.config.get("driver") == "playwright":
            try:
                from playwright.sync_api import sync_playwright
            except ImportError as exc:
                raise ImportError("Playwright is not installed. Install it with 'pip install playwright'.") from exc
            pw = sync_playwright().start()
            browser = pw.chromium.launch(headless=True)
            return browser.new_page()
        else:
            raise ValueError("Unsupported driver")