import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.accordion import Accordion


def test_visible_accordion(browser):
    page = Accordion(browser)
    page.visit()

    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(page.SECTION1_CONTENT_P)
    )
    assert page.section1_content_p.is_displayed(), "Ожидали, что section1Content > p виден по умолчанию"

    page.section1_heading.click()
    time.sleep(2)

    assert not page.section1_content_p.is_displayed(), "Ожидали, что section1Content > p скрыт после клика"


def test_visible_accordion_default(browser):
    page = Accordion(browser)
    page.visit()

    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(page.SECTION2_P1)
    )
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(page.SECTION2_P2)
    )
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(page.SECTION3_P)
    )

    assert not page.section2_p1.is_displayed(), "Ожидали, что section2Content > p:nth-child(1) скрыт по умолчанию"
    assert not page.section2_p2.is_displayed(), "Ожидали, что section2Content > p:nth-child(2) скрыт по умолчанию"
    assert not page.section3_p.is_displayed(),  "Ожидали, что section3Content > p скрыт по умолчанию"
