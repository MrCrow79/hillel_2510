import pytest

from core.ui.sausedemo.pages.login_page import LoginPage
from core.ui.sausedemo.pages.product_page import ProductsPage
from setting import d_settings


@pytest.fixture
def product_page(driver) -> ProductsPage:
    return LoginPage(driver).open_page().login(d_settings.sausedemo_user_name, d_settings.sausedemo_pwd)