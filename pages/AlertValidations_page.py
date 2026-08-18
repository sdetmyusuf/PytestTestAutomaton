from core.config_manager import ConfigManager
from pages.base_page import BasePage


class AlertValidationsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver) 
        # Load base URL from config.yaml
        config = ConfigManager.load_config()
        self.base_url = config.get("app", {}).get("base_url", "http://localhost:8000")


    def open(self):
        # Use environment‑specific base URL
        self.driver.get(f"{self.base_url}/")
        self.driver.maximize_window()


    def get_alert_message(self):
        self.wait_for_element("xpath", "//input[@id='alertbtn']", 15)
        self.click("xpath", "//input[@id='alertbtn']")
        alert = self.driver.switch_to.alert
        message = alert.text
        alert.accept()
        return message

    def get_alert_message_confirm_with_name(self, name):
        self.type("xpath", "//input[@id='name']", name)
        self.wait_for_element("xpath", "//input[@id='confirmbtn']", 15)
        self.click("xpath", "//input[@id='confirmbtn']")
        alert = self.driver.switch_to.alert
        message = alert.text
        alert.accept()
        return message