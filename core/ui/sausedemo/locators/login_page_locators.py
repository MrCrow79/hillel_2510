
from selenium.webdriver.common.by import By


class LoginPageLocators:

    login_input_locator = (By.CSS_SELECTOR, '#user-name')  # tuple  з 2х елементів
    password_input_locator = (By.XPATH, '//input[@data-test="password"]') # tuple  з 2х елементів
    login_button_locator = (By.CSS_SELECTOR, '#login-button') # tuple  з 2х елементів

    red_cross = (By.XPATH, '//*[@data-prefix="fas"]') # tuple  з 2х елементів