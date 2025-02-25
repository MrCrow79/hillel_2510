import pytest
import allure

from core.api_services.swapi_ctrl import Swapi

swapi_ctrl = Swapi()

@allure.epic("API test")
@allure.feature("Swapi tests")
@allure.story("Search user")
@pytest.mark.swapi
def test_get_search_user():

    resp = swapi_ctrl.get_users(parameters={'name': 'r2', 'second_parameter': 'some_value'})

    response_data = resp.json()

    assert response_data['message'] == 'ok', 'Message is not OK'
    assert 'r2' in response_data['result'][0]['properties']['name'].lower()
