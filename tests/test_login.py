from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

def test_login_flow(hybrid_client):
    api = hybrid_client["api"]
    browser = hybrid_client["browser"]

    # API step
    payload = {"username": "testuser", "password": "password123"}
    response = api.post("/users", json=payload)
    assert response.status_code == 201

    # UI step
    login_page = LoginPage(browser)
    login_page.open()
    login_page.login()

    dashboard_page = DashboardPage(browser)
    login_page.check_radio_button_selected()
    

