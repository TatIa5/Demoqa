
from pages.elements_page import ElementsPage
def test_find_elements(browser):
    e_page = ElementsPage(browser)
    e_page.visit()
    assert e_page.btns_first_menu.check_count_elements(count=9)


