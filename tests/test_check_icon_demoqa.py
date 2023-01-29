from pages.demoqa import Demoqa

def icon_exist(browser):
    obj = Demoqa(browser)

    obj.visit()
    obj.icon.clic()
    assert obj.equal_url()
    assert obj.icon.exist()


    # browser.get('https://demoqa.com/')#переход на стр
    # icon = browser.find_element(By.CSS_SELECTOR, '#app > header > a')
    # if icon is None:
    #     print("Элемент не найден")
    # else:
    #     print("Элемент найден")
