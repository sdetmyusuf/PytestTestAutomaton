import pytest

from pages.AlertValidations_page import AlertValidationsPage

@pytest.fixture
def test_alert_flow_fix(hybrid_client):
    api = hybrid_client["api"]
    browser = hybrid_client["browser"]

    alert_page = AlertValidationsPage(browser)
    alert_page.open()
    return alert_page


def test_alert_flow(test_alert_flow_fix):
    alert_page = test_alert_flow_fix
    message = alert_page.get_alert_message()
    assert message == "Hello , share this practice page and share your knowledge", f"Unexpected alert message: {message}"

@pytest.mark.parametrize("name,expected", [("Alice", "Hello Alice, Are you sure you want to confirm?"), ("Bob", "Hello Bob, Are you sure you want to confirm?"), ("Charlie", "Hello Charlie, Are you sure you want to confirm?")])
def test_alert_flow_with_name(test_alert_flow_fix, name, expected):
    alert_page = test_alert_flow_fix
    message = alert_page.get_alert_message_confirm_with_name(name)
    assert message == expected, f"Unexpected alert message: {message}"