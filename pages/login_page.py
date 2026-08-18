from pages.base_page import BasePage
from core.config_manager import ConfigManager

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        # Load base URL from config.yaml
        config = ConfigManager.load_config()
        self.base_url = config.get("app", {}).get("base_url", "http://localhost:8000")

    def open(self):
        # Use environment‑specific base URL
        self.driver.get(f"{self.base_url}/")

    def login(self):
        self.wait_for_element("name", "radioButton", 10)
        self.click("name", "radioButton")
        from selenium.webdriver.common.by import By

    
    def check_radio_button_selected(self):
        is_sel =  self.is_radio_button_selected("name", "radioButton")
        assert is_sel, "Radio button is not selected after clicking."
        # self.type("id", "password", password)
        # self.click("css selector", "button[type='submit']")
