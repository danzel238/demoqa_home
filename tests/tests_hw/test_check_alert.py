import time
from selenium.webdriver.common.by import By


def test_timer_alert(browser):
    browser.get("https://demoqa.com/alerts")

    browser.find_element(By.CSS_SELECTOR, "#timerAlertButton").click()

    time.sleep(6)

    alert = browser.switch_to.alert
    assert "alert" in alert.text.lower()
    alert.accept()
