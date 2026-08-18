from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, locator_type, locator_value):
        self.driver.find_element(locator_type, locator_value).click()

    def type(self, locator_type, locator_value, text):
        self.driver.find_element(locator_type, locator_value).send_keys(text)

    def get_text(self, locator_type, locator_value):
        return self.driver.find_element(locator_type, locator_value).text
    
    def wait_for_element(self, locator_type, locator_value, timeout=10):
        """
        Wait for an element to be present on the page.
        """

        locator = (getattr(By, locator_type.upper()), locator_value)
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
    
    
    def is_radio_button_selected(self, locator_type, locator_value):
        """
        Check if a radio button is selected.
        """
        radio_button = self.driver.find_element(locator_type, locator_value)
        return radio_button.is_selected()
    
    def select_options_by_visible_text(self, locator_type, locator_value, text):
        """
        Select an option from a dropdown by visible text.
        """
        select_element = self.driver.find_element(locator_type, locator_value)
        select = Select(select_element)
        select.select_by_visible_text(text)


    def verify_selected_option(self, locator_type, locator_value, expected_text):
        """
        Verify that the selected option in a dropdown matches the expected text.
        """
        select_element = self.driver.find_element(locator_type, locator_value)
        select = Select(select_element)
        # selected_option = select.first_selected_option.text
        # return selected_option == expected_text
        selected_value = select.first_selected_option.text  # Get the text of the first selected option in the dropdown
        
        print(f"Selected value: {selected_value}")
        assert selected_value == expected_text