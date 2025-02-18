import pytest
from selenium.webdriver import Chrome

from core.ui.sausedemo.pages.login_page import LoginPage


# scopes
# function = by default, для кожного тесту
# class = для класу
# module = для файлу
# package = для папки
# session  = для всіх тестів в запуску


@pytest.fixture
def driver():
    driver = Chrome()
    yield driver
    driver.close()
