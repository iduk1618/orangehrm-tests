import pytest
from pages.login_page import LoginPage
from utils import config

def test_valid_login(browser):
    login_page = LoginPage(browser)
    login_page.load(config.BASE_URL)
    login_page.login(config.USERNAME, config.PASSWORD)
    assert "dashboard" in browser.current_url.lower()

def test_invalid_login(browser):
    login_page = LoginPage(browser)
    login_page.load(config.BASE_URL)
    login_page.login("pogresan_user", "pogresan_pass")
    
    browser.save_screenshot("screenshots/debug_invalid_login.png")

    assert "Invalid credentials" in login_page.get_error_message()