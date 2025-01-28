import pytest
import time

from core.api_services.gorest_ctrl import Gorest


gorest_ctrl = Gorest()


@pytest.mark.gorest
def test_create_user_negative():

    user_body = {
    }

    gorest_ctrl.create_user(user_body=user_body, expected_status_code=422)


@pytest.mark.gorest
@pytest.mark.parametrize('auth_header', [
    {}, # no auth headers
    {'Authorization': 'asd'} # wrong auth header
], ids=['no auth headers', 'wrong auth header'])
def test_create_user_auth_negative(auth_header):

    user_body = {
        "name":"Tenali Ramakrishna",
        "gender":"male",
        "email":f"tenali.ramakrishna@{time.time()}.com",
        "status":"active"
    }

    gorest_ctrl.create_user(user_body=user_body, extra_auth_token=auth_header, expected_status_code=401)


