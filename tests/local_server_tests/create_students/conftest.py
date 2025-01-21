import pytest


@pytest.fixture(scope='session')
def auth_header(local_server_ctrl):

    return local_server_ctrl.auth(json={"name": "test", "password": "test"}).text