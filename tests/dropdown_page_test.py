from pages.dropdown_page import DropDownPage

def test_dropdown_flow(hybrid_client):
    api = hybrid_client["api"]
    browser = hybrid_client["browser"]

    dropdown_page = DropDownPage(browser)
    dropdown_page.open()
    # Select an option from the dropdown
    dropdown_page.select_option("Option1")
    # Verify the selected option
    is_correct = dropdown_page.verify_selected_option_dropdown()
    print(f"Is the correct option selected? {is_correct}")
    assert is_correct, "Incorrect option selected in the dropdown."