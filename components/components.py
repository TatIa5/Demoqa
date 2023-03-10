from selenium.webdriver.common.by import By
from selenium.common import NoSuchFrameException
from selenium.common import NoSuchFrameException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WebElement():
    def __init__(self, driver, locator = ''):
        self.driver = driver
        self.locator = locator

    def click(self):
        self.find_element().click() #действие


    def find_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.locator)

    def find_elements(self):
        return self.driver.find_elements(By.CSS_SELECTOR, self.locator)

    def check_count_elements(self, count: int) -> bool:
        if len(self.find_elements()) == count:
            return True
        return False


    def exist(self):
        try:
            self.find_element()
        except NoSuchFrameException:
            return False
        return True

    def get_text(self):
        return str(self.find_element().text)

    def visible(self):
        return self.find_element().is_displayed()

    def not_visible(self, time_wait = 2):
        try:
            WebDriverWait(self.driver, time_wait).until_not(EC.invisibility_of_element((By.CSS_SELECTOR, self.locator)))
            return False
        except TimeoutException:
            return True
