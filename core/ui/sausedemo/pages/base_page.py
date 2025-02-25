from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import allure

import logging

from core.ui.sausedemo.utils.custom_condition import WaitNElements


class BasePage:

    def __init__(self, driver, url):
        self._driver = driver
        self.url = url
        self.logger = logging.getLogger()

    def open_page(self):
        allure.step(f'{__class__.__name__} opening ')
        self._driver.get(self.url)
        self.logger.info(f'Page {__class__.__name__} was opened')
        return self

    def get_n_elements_presents(self, locator, quantity_of_elements, timeout=2, message=''):

        self.logger.info(f'Checking {quantity_of_elements} elements  for {quantity_of_elements} locator')

        return WebDriverWait(self._driver, timeout=timeout).until(
            WaitNElements(locator=locator, quantity=quantity_of_elements),
            message=message)

    def _elements_present(self, locator, timeout=2, message=''):
        return WebDriverWait(self._driver, timeout=timeout).until(
            EC.presence_of_all_elements_located(locator),
            message=message)

    def _element_present(self, locator, timeout=2, message=''):
        return WebDriverWait(self._driver, timeout=timeout).until(
            EC.presence_of_element_located(locator),
            message=message)

    def _element_clickable(self, locator, timeout=2, message=''):
        return WebDriverWait(self._driver, timeout=timeout).until(
            EC.element_to_be_clickable(locator),
            message=message)
