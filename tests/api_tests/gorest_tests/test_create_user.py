import time

import allure

from setting import d_settings
from tests.api_tests.gorest_tests.base_gorest import BaseGorestTest


@allure.story("Create user")
class TestCreateUser(BaseGorestTest):

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Create base user')
    def test_create_user(self):
        """ some description of tests test_create_user"""

        user_body = {
            "name":"Tenali Ramakrishna",
            "gender":"male",
            "email":f"tenali.ramakrishna@{time.time()}.com",
            "status":"active"
        }

        self.gorest_ctrl.create_user(user_body=user_body, headers={'User-Agent': 'Custom-user-agent'})


    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Additional test for working with .env')
    def test_work_with_env(self):

        assert d_settings.DATABASE_URL == 'postgresql://den:den@localhost:5432/new_db'


