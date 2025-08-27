from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class WebTables(BasePage):
    base_url = "https://demoqa.com/webtables"


    ADD_BTN = (By.ID, "addNewRecordButton")
    MODAL = (By.CSS_SELECTOR, ".modal-content")
    SUBMIT = (By.ID, "submit")


    FN = (By.ID, "firstName")
    LN = (By.ID, "lastName")
    EMAIL = (By.ID, "userEmail")
    AGE = (By.ID, "age")
    SALARY = (By.ID, "salary")
    DEPT = (By.ID, "department")


    ROWS = (By.CSS_SELECTOR, ".rt-tbody .rt-tr-group")
    LAST_ROW_TDS = (By.CSS_SELECTOR, ".rt-tbody .rt-tr-group:last-child .rt-td")
    LAST_ROW_EDIT = (By.CSS_SELECTOR, ".rt-tbody .rt-tr-group:last-child [id^='edit-record-']")
    LAST_ROW_DELETE = (By.CSS_SELECTOR, ".rt-tbody .rt-tr-group:last-child [id^='delete-record-']")


    def open_add(self):
        by, value = self.ADD_BTN
        self.driver.find_element(by, value).click()

    def submit(self):
        by, value = self.SUBMIT
        self.driver.find_element(by, value).click()

    def modal_visible(self) -> bool:
        by, value = self.MODAL
        els = self.driver.find_elements(by, value)
        return bool(els and els[0].is_displayed())

    def _clear_and_type(self, locator, text: str):
        by, value = locator
        el = self.driver.find_element(by, value)
        el.clear()
        el.send_keys(text)

    def fill_form(self, first, last, email, age, salary, dept):
        self._clear_and_type(self.FN, str(first))
        self._clear_and_type(self.LN, str(last))
        self._clear_and_type(self.EMAIL, str(email))
        self._clear_and_type(self.AGE, str(age))
        self._clear_and_type(self.SALARY, str(salary))
        self._clear_and_type(self.DEPT, str(dept))

    def rows_count(self) -> int:
        by, value = self.ROWS
        return len(self.driver.find_elements(by, value))

    def last_row_values(self):
        # Порядок: First Name, Last Name, Age, Email, Salary, Department, Action
        by, value = self.LAST_ROW_TDS
        tds = self.driver.find_elements(by, value)
        return [td.text for td in tds[:6]]

    def edit_last_row(self):
        by, value = self.LAST_ROW_EDIT
        self.driver.find_element(by, value).click()

    def delete_last_row(self):
        by, value = self.LAST_ROW_DELETE
        self.driver.find_element(by, value).click()

    def form_values(self):
       
        by, value = self.FN
        fn = self.driver.find_element(by, value).get_attribute("value")

        by, value = self.LN
        ln = self.driver.find_element(by, value).get_attribute("value")

        by, value = self.AGE
        age = self.driver.find_element(by, value).get_attribute("value")

        by, value = self.EMAIL
        email = self.driver.find_element(by, value).get_attribute("value")

        by, value = self.SALARY
        salary = self.driver.find_element(by, value).get_attribute("value")

        by, value = self.DEPT
        dept = self.driver.find_element(by, value).get_attribute("value")

        return [fn, ln, age, email, salary, dept]
