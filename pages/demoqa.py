from components.components import WebElement
from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException

class DemoQa(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/'
        super().__init__(driver, self.base_url)

        self.icon = WebElement(driver,'#app > header > a' )
        self.btn_elements = WebElement (driver, "#app > div > div > div.home-body > div > div:nth-child(1)")

    def exist_icon(self):
        try:
            self.icon.find_element()
        except NoSuchElementException:
            return False
        return True


    def equal_url(self):
        if self.get_url() == self.base_url:
            return True
        else:
            return False
