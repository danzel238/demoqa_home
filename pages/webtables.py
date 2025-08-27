from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class WebTables(BasePage):
    base_url = "https://demoqa.com/webtables"

    def open_add(self):
        self.driver.find_element(By.CSS_SELECTOR, "#addNewRecordButton").click()

    def submit(self):
        self.driver.find_element(By.CSS_SELECTOR, "#submit").click()

    def modal_visible(self) -> bool:
        modals = self.driver.find_elements(By.CSS_SELECTOR, ".modal-content")
        return bool(modals and modals[0].is_displayed())

    def fill_form(self, first, last, email, age, salary, dept):
        self.driver.find_element(By.CSS_SELECTOR, "#firstName").clear()
        self.driver.find_element(By.CSS_SELECTOR, "#firstName").send_keys(first)

        self.driver.find_element(By.CSS_SELECTOR, "#lastName").clear()
        self.driver.find_element(By.CSS_SELECTOR, "#lastName").send_keys(last)

        self.driver.find_element(By.CSS_SELECTOR, "#userEmail").clear()
        self.driver.find_element(By.CSS_SELECTOR, "#userEmail").send_keys(email)

        self.driver.find_element(By.CSS_SELECTOR, "#age").clear()
        self.driver.find_element(By.CSS_SELECTOR, "#age").send_keys(str(age))

        self.driver.find_element(By.CSS_SELECTOR, "#salary").clear()
        self.driver.find_element(By.CSS_SELECTOR, "#salary").send_keys(str(salary))

        self.driver.find_element(By.CSS_SELECTOR, "#department").clear()
        self.driver.find_element(By.CSS_SELECTOR, "#department").send_keys(dept)

    def rows_count(self) -> int:
        return len(self.driver.find_elements(By.CSS_SELECTOR, ".rt-tbody .rt-tr-group"))

    def last_row_values(self):
        tds = self.driver.find_elements(
            By.CSS_SELECTOR, ".rt-tbody .rt-tr-group:last-child .rt-td"
        )
        return [td.text for td in tds[:6]]

    def edit_last_row(self):
        self.driver.find_element(
            By.CSS_SELECTOR, ".rt-tbody .rt-tr-group:last-child [id^='edit-record-']"
        ).click()

    def delete_last_row(self):
        self.driver.find_element(
            By.CSS_SELECTOR, ".rt-tbody .rt-tr-group:last-child [id^='delete-record-']"
        ).click()

    def form_values(self):
        fn = self.driver.find_element(By.CSS_SELECTOR, "#firstName").get_attribute("value")
        ln = self.driver.find_element(By.CSS_SELECTOR, "#lastName").get_attribute("value")
        age = self.driver.find_element(By.CSS_SELECTOR, "#age").get_attribute("value")
        email = self.driver.find_element(By.CSS_SELECTOR, "#userEmail").get_attribute("value")
        salary = self.driver.find_element(By.CSS_SELECTOR, "#salary").get_attribute("value")
        dept = self.driver.find_element(By.CSS_SELECTOR, "#department").get_attribute("value")
        return [fn, ln, age, email, salary, dept]
