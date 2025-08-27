from selenium.webdriver.common.by import By

def test_sort_all_headers(browser):
    browser.get("https://demoqa.com/webtables")


    headers = browser.find_elements(By.CSS_SELECTOR, ".rt-table .rt-thead.-header .rt-th")[:6]

    for header in headers:
      
        header.click()
        assert "sort-asc" in header.get_attribute("class")

     
        header.click()
        assert "sort-desc" in header.get_attribute("class")
