import pytest
import time
import allure

from core.api_services.gorest_ctrl import Gorest


from tests.api_tests.gorest_tests.base_gorest import BaseGorestTest


@allure.story("Negative")
@allure.severity(allure.severity_level.MINOR)
class TestGorestNegative(BaseGorestTest):

    @pytest.mark.gorest
    def test_create_user_negative(self):

        user_body = {
        }

        self.gorest_ctrl.create_user(user_body=user_body, expected_status_code=422)


    @pytest.mark.gorest
    @pytest.mark.parametrize('auth_header', [
        {}, # no auth headers
        {'Authorization': 'asd'} # wrong auth header
    ], ids=['no auth headers', 'wrong auth header'])
    def test_create_user_auth_negative(self, auth_header):

        user_body = {
            "name":"Tenali Ramakrishna",
            "gender":"male",
            "email":f"tenali.ramakrishna@{time.time()}.com",
            "status":"active"
        }

        self.gorest_ctrl.create_user(user_body=user_body, extra_auth_token=auth_header, expected_status_code=401)


