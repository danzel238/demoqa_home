from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ModalDialogs(BasePage):
    base_url = "https://demoqa.com/modal-dialogs"

    SUBMENU_ITEMS = (By.CSS_SELECTOR, ".btn.btn-light")  
    HOME_ICON = (By.CSS_SELECTOR, "header a.navbar-brand")  

  
    def submenu_items(self):
        return self.driver.find_elements(*self.SUBMENU_ITEMS)

    def count_submenu_items(self) -> int:
        return len(self.submenu_items())

    def home_icon(self):
        return self.driver.find_element(*self.HOME_ICON)
