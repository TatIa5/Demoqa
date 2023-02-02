from pages.demoqa import Demoqa
from pages.elements_page import ElementsPage


def test_navigation(browser):
    obj = Demoqa(browser)
    obj1 = ElementsPage(browser)
    obj.btn_elements.click()
    obj.visit()
    obj1.refresh()
    browser.refresh()
    browser.back()
    browser.forward()
    assert obj1.equal_url()
