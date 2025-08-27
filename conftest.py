import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome()
    yield driver
    browser.set_window_size(1000,1000)
    driver.quit()
