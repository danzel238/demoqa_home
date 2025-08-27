from selenium.webdriver.common.by import By
import pytest


def _is_page_available(driver, url: str) -> bool:
    try:
        driver.get(url)
    except Exception:
        return False
    return "demoqa.com" in driver.current_url.lower()


def test_check_modal(browser):
    url = "https://demoqa.com/modal-dialogs"
    if not _is_page_available(browser, url):
        pytest.skip("Страница недоступна")

    # Small modal
    browser.find_element(By.CSS_SELECTOR, "#showSmallModal").click()
    assert browser.find_element(By.CSS_SELECTOR, ".modal-content").is_displayed()
    browser.find_element(By.CSS_SELECTOR, "#closeSmallModal").click()

    # Large modal
    browser.find_element(By.CSS_SELECTOR, "#showLargeModal").click()
    assert browser.find_element(By.CSS_SELECTOR, ".modal-content").is_displayed()
    browser.find_element(By.CSS_SELECTOR, "#closeLargeModal").click()
