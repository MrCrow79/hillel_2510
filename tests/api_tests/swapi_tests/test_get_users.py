import pytest

from core.api_services.swapi_ctrl import Swapi

swapi_ctrl = Swapi()


@pytest.mark.swapi
def test_get_users():

    resp = swapi_ctrl.get_users()