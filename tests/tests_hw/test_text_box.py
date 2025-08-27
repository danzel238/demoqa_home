from selenium.webdriver.common.by import By


def test_text_box(browser):
    # a. перейти на страницу
    browser.get("https://demoqa.com/text-box")

    # b. записать в поля Full Name и Current Address произвольный текст
    full_name_input = browser.find_element(By.ID, "userName")
    address_input = browser.find_element(By.ID, "currentAddress")

    full_name_input.send_keys("Иван Иванов")
    address_input.send_keys("Москва, Тверская 1")

    # c. нажать на кнопку submit
    submit_btn = browser.find_element(By.ID, "submit")
    submit_btn.click()

    # d. проверить, что снизу появились элементы с нашим текстом
    output_name = browser.find_element(By.ID, "name").text
    output_address = browser.find_element(By.ID, "currentAddress").text

    assert page.output_name_text() == f"Name:{name}"
    assert page.output_current_address_text() == f"Current Address :{address}"
