import pytest
import allure

from core.api_services.swapi_ctrl import Swapi

swapi_ctrl = Swapi()

@allure.epic("API test")
@allure.feature("Swapi tests")
@allure.story("Negative")
@allure.title('Get get user negative cases')
@pytest.mark.swapi
def test_get_users_negative():

    swapi_ctrl.get_user(user_id=100500, expected_status_code=404)

@allure.epic("API test")
@allure.feature("Swapi tests")
@allure.title('Get get user negative cases case 2')
@pytest.mark.swapi
def test_get_users_negative_without_check_status_code():

    swapi_ctrl.get_user(user_id=100500, expected_status_code=None)