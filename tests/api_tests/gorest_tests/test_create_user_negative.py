import pytest

from core.api_services.gorest_ctrl import Gorest


gorest_ctrl = Gorest()


@pytest.mark.gorest
def test_create_user_negative():

    user_body = {
    }

    gorest_ctrl.create_user(user_body=user_body, expected_status_code=422)


