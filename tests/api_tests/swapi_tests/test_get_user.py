import pytest

from core.api_services.swapi_ctrl import Swapi
import allure

swapi_ctrl = Swapi()


@allure.title('Get user and check uuid is correct')

@allure.tag("SWAPI_TESTS", "GET_USERS")
@allure.severity(allure.severity_level.TRIVIAL)
@allure.label("owner", "John Doe")
@allure.link("https://dev.example.com/", name="Website")
@pytest.mark.swapi
@pytest.mark.parametrize('user_id', [1,2,3])
def test_get_user(user_id):
    allure.description(
        "Test that gets user by user_id and checks user)id of response and Message field in response body")

    allure.epic("API test")
    allure.feature("Swapi tests")
    allure.story("Get user")


    resp = swapi_ctrl.get_user(user_id)

    response_data = resp.json()

    assert response_data['message'] == 'ok', 'Message is not OK'
    assert int(response_data['result']['uid']) == user_id, \
        f'user_id should be {user_id}, but its {response_data["result"]["uid"]}'

@allure.epic("API test")
@allure.feature("Swapi tests")
@allure.story("Get Planets")
@allure.title('Get planets')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.swapi
@pytest.mark.parametrize('planets_id', [1,2,3])
def test_get_planets(planets_id):

    resp = swapi_ctrl.get_planet(planets_id)

    response_data = resp.json()

    assert response_data['message'] == 'ok', 'Message is not OK'
    assert int(response_data['result']['uid']) == planets_id, \
        f'user_id should be {planets_id}, but its {response_data["result"]["uid"]}'


    # print(resp)
    #
    # print('headers', resp.headers)
    # print('headers dict', dict(resp.headers))
    # print('text', resp.text)
    # print('json', resp.json())  # json.loads(resp.text)
    # print('status_code', resp.status_code)

