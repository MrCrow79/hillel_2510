import pytest

from core.api_services.gorest_ctrl import Gorest
import allure

@allure.epic("API test")
@allure.feature("Gorest tests")
@pytest.mark.gorest
class BaseGorestTest:
    gorest_ctrl = Gorest()



