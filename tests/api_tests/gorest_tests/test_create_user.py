import pytest

from core.api_services.gorest_ctrl import Gorest
import time

gorest_ctrl = Gorest()


@pytest.mark.gorest
def test_create_user():

    user_body = {
        "name":"Tenali Ramakrishna",
        "gender":"male",
        "email":f"tenali.ramakrishna@{time.time()}.com",
        "status":"active"
    }

    gorest_ctrl.create_user(user_body=user_body, headers={'User-Agent': 'Custom-user-agent'})


