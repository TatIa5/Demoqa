from pages.elements_page import ElementsPage
import time
from pages.accordian_page import AccordianPage
def test_visible_btn_sidebar(browser):  #отрабатывает видимость элемента
    elements_page = ElementsPage(browser)
    elements_page.visit()
    elements_page.btn_sidebar_first.click()
    time.sleep(3)
    assert elements_page.btn_sidebar_first.visible()


def test_visible_accordion(browser):
    accordian_page = AccordianPage(browser)
    accordian_page.visit()
    assert accordian_page.content_p.visible()
    accordian_page.btn_section1.click()
    time.sleep(2)
    assert accordian_page.content_p.not_visible(2)





