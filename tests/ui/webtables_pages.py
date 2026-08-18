from core.config_manager import ConfigManager
from pages.base_page import BasePage


class TestWebTablesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        config = ConfigManager.load_config()
        self.base_url = config.get("app", {}).get("base_url", "http://localhost:8000")

    def open(self):
        self.driver.get(f"{self.base_url}/")
        self.driver.maximize_window()

    def get_table_data(self):
        table_data = []
        rows = self.driver.find_elements("xpath", "//table[@class='table table-striped']/tbody/tr")
        for row in rows:
            cells = row.find_elements("tag name", "td")
            row_data = [cell.text for cell in cells]
            table_data.append(row_data)
        return table_data