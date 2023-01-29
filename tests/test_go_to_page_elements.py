from pages.demoqa import Demoqa
from pages.elements_page import ElementsPage


def test_go_to_page_elements(browser):
    obj = Demoqa(browser)
    elements_page = ElementsPage(browser)
    obj.visit()
    assert obj.equal_url()
    obj.btn_elements.click()
    assert elements_page.equal_url()