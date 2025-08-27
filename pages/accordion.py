from selenium.webdriver.common.by import By

class Accordion:
    def __init__(self, browser):
        self.browser = browser
        self.url = "https://demoqa.com/accordian"

        # Локаторы
        self.SECTION1_CONTENT_P = (By.CSS_SELECTOR, "#section1Content > p")
        self.SECTION1_HEADING   = (By.CSS_SELECTOR, "#section1Heading")

        self.SECTION2_P1 = (By.CSS_SELECTOR, "#section2Content > p:nth-child(1)")
        self.SECTION2_P2 = (By.CSS_SELECTOR, "#section2Content > p:nth-child(2)")
        self.SECTION3_P  = (By.CSS_SELECTOR, "#section3Content > p")


    def visit(self):
        self.browser.get(self.url)

  
    @property
    def section1_content_p(self):
        return self.browser.find_element(*self.SECTION1_CONTENT_P)

    @property
    def section1_heading(self):
        return self.browser.find_element(*self.SECTION1_HEADING)

    @property
    def section2_p1(self):
        return self.browser.find_element(*self.SECTION2_P1)

    @property
    def section2_p2(self):
        return self.browser.find_element(*self.SECTION2_P2)

    @property
    def section3_p(self):
        return self.browser.find_element(*self.SECTION3_P)
