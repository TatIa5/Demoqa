from pages.demoqa import Demoqa
from pages.elements_page import ElementsPage

def test_check_text_please(browser):   #создали метод get_text ф (0) Экземпляр 1 стр,2й стр
    obj = Demoqa(browser)
    elements_page = ElementsPage(browser)
    obj.visit()
    obj.btn_elements.click()
    assert elements_page.text_please.get_text() == 'Please select an item from left to start practice.'  #получаем текст из элемента и


def test_page_elements(browser):
    elements_page = ElementsPage(browser)
    elements_page.visit()
    assert elements_page.text_please2.get_text() == 'Elements'