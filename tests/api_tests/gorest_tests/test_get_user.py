from core.api_services.gorest_ctrl import Gorest

gorest_ctrl = Gorest()


def test_get_user():

    gorest_ctrl.get_user(5, expected_status_code=404)


