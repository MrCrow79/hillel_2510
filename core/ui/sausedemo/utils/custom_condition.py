from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class WaitNElements:
    def __init__(self, locator, quantity):
        self.locator = locator
        self.quantity = quantity

    def __call__(self, driver):
        try:
            element = driver.find_elements(*self.locator)   # find_elements завжди повертае список елементів, якщо елементів не знайдено, то пожній список
            return len(element) == self.quantity
        except:
            return False
