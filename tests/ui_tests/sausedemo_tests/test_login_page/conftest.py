import pytest

from core.ui.sausedemo.pages.login_page import LoginPage


@pytest.fixture
def login_page(driver):
    login_page = LoginPage(driver)
    login_page.open_page()
    return login_page