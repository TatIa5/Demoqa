
from pages.elements_page import ElementsPage
def test_elements_dz(browser):
    e_page = ElementsPage(browser)
    e_page.visit()
    assert e_page.ul_menu.check_count_elements(5)


def test_navigation_dz(browser):
    e_page = ElementsPage(browser)
    e_page.refresh()
    e_page.btn_alerts.click()
    e_page.visit()
    e_page.back()
    browser.set_window_size(900, 400)
    e_page.forward()
    assert e_page.equal_url()
    browser.set_window_size(1000, 1000)


