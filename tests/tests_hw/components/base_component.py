from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseComponent:
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator

    def find_element(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.locator)
        )

    def get_text(self):
        return str(self.find_element().text)

    def is_displayed(self):
        return self.find_element().is_displayed()

    def click(self):
        self.find_element().click()