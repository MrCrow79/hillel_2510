import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from core.ui.sausedemo.login_page_locators import LoginPageLocators
from core.ui.sausedemo.pages.product_page import ProductsPage
from core.ui.sausedemo.product_page_locators import ProductPageLocators
from setting import d_settings


from core.ui.sausedemo.pages.base_page import BasePage
from setting import d_settings


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver=driver, url=d_settings.sauserdemo_url)


    def _user_name_input(self, timeout):
        return self._element_present(locator=LoginPageLocators.login_input_locator, timeout=timeout,
                                     message='Cant find user input on logint page')


    def _password_input(self):
        return self._element_present(locator=LoginPageLocators.password_input_locator, timeout=2,
                                     message='Cant find user password on logint page')

    def _login_button(self, timeout=3):
        return self._element_clickable(locator=LoginPageLocators.login_button_locator, timeout=timeout,
                                     message='Cant find login button on logint page')


    def check_creds_are_wrong(self, timeout=1):
        assert self._driver.current_url == self.url, f'expected current url is {self.url}'

        self.get_n_elements_presents(locator=LoginPageLocators.red_cross, quantity_of_elements=4,
                                     timeout=timeout, message='Cant find red cross if user input wrong creds')


    def set_user_name(self, username, timeout=2):
        self._user_name_input(timeout=timeout).send_keys(username)
        return self

    def set_user_pwd(self, userpwd):
        self._password_input().send_keys(userpwd)
        return self


    def click_login(self):
        self._login_button().click()
        return self

    # positive cases
    def login(self, username, userpwd) -> ProductsPage:
        self.set_user_name(username).set_user_pwd(userpwd).click_login()
        return ProductsPage(self._driver)




