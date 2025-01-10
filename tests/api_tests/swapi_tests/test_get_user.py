import pytest

from core.api_services.swapi_ctrl import Swapi

swapi_ctrl = Swapi()


@pytest.mark.swapi
@pytest.mark.parametrize('user_id', [1,2,3])
def test_get_user(user_id):

    resp = swapi_ctrl.get_user(user_id)

    response_data = resp.json()

    assert response_data['message'] == 'ok', 'Message is not OK'
    assert int(response_data['result']['uid']) == user_id, \
        f'user_id should be {user_id}, but its {response_data["result"]["uid"]}'


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

