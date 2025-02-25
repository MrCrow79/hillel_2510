import allure

from tests.api_tests.gorest_tests.base_gorest import BaseGorestTest


@allure.story("Get user")
@allure.severity(allure.severity_level.CRITICAL)
class TestGetUser(BaseGorestTest):

    def test_get_user(self):

        self.gorest_ctrl.get_user(5, expected_status_code=404)


