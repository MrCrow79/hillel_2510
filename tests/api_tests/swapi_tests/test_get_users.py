import pytest
import allure

from core.api_services.swapi_ctrl import Swapi

swapi_ctrl = Swapi()

@allure.epic("API test")
@allure.feature("Swapi tests")
@allure.story("Get users")
@allure.title('Get get all users')
@pytest.mark.swapi
def test_get_users():

    resp = swapi_ctrl.get_users()