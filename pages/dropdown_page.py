from pages.base_page import BasePage
from core.config_manager import ConfigManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class DropDownPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        # Load base URL from config.yaml
        config = ConfigManager.load_config()
        self.base_url = config.get("app", {}).get("base_url", "http://localhost:8000")

    def open(self):
        # Use environment‑specific base URL
        self.driver.get(f"{self.base_url}/")
        self.driver.maximize_window()


    def select_option(self, option_text):
        # self.wait_for_element("id", "dropdown-class-example", 15)
        # self.click("id", "dropdown-class-example")
        # option_locator = f"//option[text()='{option_text}']"
        # self.wait_for_element("xpath", option_locator)
        # self.click("xpath", option_locator)
        self.select_options_by_visible_text("id", "dropdown-class-example", option_text)

    def verify_selected_option_dropdown(self):
        print("Verifying the selected option in the dropdown...")
        self.verify_selected_option("id", "dropdown-class-example", "Option1")
        # self.wait_for_element("id", "dropdown-class-example")
        # return self.verify_selected_option("id", "dropdown-class-example", "Option1")
