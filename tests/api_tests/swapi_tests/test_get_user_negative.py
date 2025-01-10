import pytest

from core.api_services.swapi_ctrl import Swapi

swapi_ctrl = Swapi()


@pytest.mark.swapi
def test_get_users_negative():

    swapi_ctrl.get_user(user_id=100500, expected_status_code=404)


@pytest.mark.swapi
def test_get_users_negative_without_check_status_code():

    swapi_ctrl.get_user(user_id=100500, expected_status_code=None)