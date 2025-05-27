import pytest
from pages.login_page import LoginPage

def test_login_valid_user(setup):
    driver = setup
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("admin", "admin123")
    assert "Dashboard" in driver.title