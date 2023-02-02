from pages.base_page import BasePage
from components.components import WebElement
class AccordianPage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian'
        super().__init__(driver, self.base_url)

        self.content_p = WebElement(driver, '#section1Content > p') #экземпляр
        self.btn_section1 = WebElement(driver, '#section1Heading')