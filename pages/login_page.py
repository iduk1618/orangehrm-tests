from .base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.username_input = (By.NAME, "username")
        self.password_input = (By.NAME, "password")
        self.login_button = (By.XPATH, "//button[@type='submit']")

    def load(self, base_url):
        self.driver.get(base_url)

    def login(self, username, password):
        self.type(self.username_input, username)
        self.type(self.password_input, password)
        self.click(self.login_button)
        self.wait_for_url("dashboard")

    def get_error_message(self):
        error_locator = (By.XPATH, "//p[contains(., 'Invalid credentials')]")
        return self.get_text(error_locator)