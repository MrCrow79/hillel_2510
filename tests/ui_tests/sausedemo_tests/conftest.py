import os

import pytest
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver import Firefox, FirefoxOptions


# chromedriver_autoinstaller.install()
from core.ui.sausedemo.pages.login_page import LoginPage


# scopes
# function = by default, для кожного тесту
# class = для класу
# module = для файлу
# package = для папки
# session  = для всіх тестів в запуску


@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.close()


def get_driver():

    if os.getenv('browser', 'chrome') == 'chrome':  # передаю в evn vars browser=chrome або не передаю нічого
        options = ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        options.browser_version = "114"
        return Chrome(options=options)

    options = FirefoxOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    return Firefox(options=options)
