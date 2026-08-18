from pages.base_page import BasePage

class DashboardPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def is_loaded(self) -> bool:
        """
        Verify that the dashboard page is loaded.
        This can be done by checking for a unique element on the dashboard.
        """
        try:
            element = self.driver.find_element("css selector", "h1.dashboard-title")
            return element.is_displayed()
        except Exception:
            return False

    def get_welcome_message(self) -> str:
        """
        Return the welcome message text displayed on the dashboard.
        """
        return self.get_text("css selector", "div.welcome-message")

    def navigate_to_profile(self):
        """
        Click on the profile link in the dashboard.
        """
        self.click("css selector", "a#profile-link")

    def logout(self):
        """
        Perform logout action from the dashboard.
        """
        self.click("css selector", "button#logout")
