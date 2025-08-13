from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type(self, locator, text):
        self.find(locator).send_keys(text)

    def load(self, url):
        self.driver.get(url)

    def wait_for_url(self, partial_url):
        self.wait.until(EC.url_contains(partial_url))

    def get_text(self, locator):
        return self.wait.unitl(EC.visibility_of_element_located(locator)).text