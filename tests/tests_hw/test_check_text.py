from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.tests_hw.components.base_component import BaseComponent


def test_footer_text(driver):
    driver.get("https://demoqa.com/")

    footer_locator = (By.XPATH, "//footer//span")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(footer_locator))

    footer_component = BaseComponent(driver, footer_locator)
    actual_text = footer_component.get_text()
    expected_text = "© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED."

    assert actual_text == expected_text, (
        f"Ожидался текст: '{expected_text}', но получен: '{actual_text}'"
    )


def test_center_text_on_elements_page(driver):
    driver.get("https://demoqa.com/")

    elements_button_locator = (
        By.XPATH,
        "//div[@class='card-body']//h5[text()='Elements']",
    )
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(elements_button_locator)
    )

    elements_button = BaseComponent(driver, elements_button_locator)
    elements_button.click()

    assert "elements" in driver.current_url.lower(), "Не удалось перейти на страницу Elements"

    center_text_locator = (
        By.XPATH,
        "//div[contains(@class,'col-md-6')]//div[contains(text(),'Please select an item')]",
    )
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(center_text_locator)
    )

    center_text_component = BaseComponent(driver, center_text_locator)
    actual_text = center_text_component.get_text()
    expected_text = "Please select an item from left to start practice."

    assert actual_text == expected_text, (
        f"Ожидался текст: '{expected_text}', но получен: '{actual_text}'"
    )
