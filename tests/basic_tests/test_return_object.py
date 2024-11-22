import unittest

import random
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent))


from core.asserts.function_asserts import assert_user

def get_user_data(user_id):

    user_data = {
        1: {'id': 1, 'name': 'Denys', 'companies': ['company_1', 'company_3', 'company_2']},
        2: {'id': 2, 'name': 'Ivan', 'companies': ['company_1', 'company_5']},
        3: {'id': 3, 'name': 'Sofa', 'companies': ['company_1', ]}
    }

    return user_data[user_id]


class GetUserDataTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.class_random_value = random.random()
        print(f'Setup value before all tests in class , value is {cls.class_random_value}')

    @classmethod
    def tearDownClass(cls):
        print(f'Setup value after all tests in class')



    def setUp(self):
        self.random_value = random.random()
        print(f'Setup value before function, values is {self.random_value}')

    def tearDown(self):
        print('Setup value after function')


    def test_get_user_id_1(self):

        print(f'Set was started, value = {self.random_value}')
        user_id = 1
        user_name = 'Denys'
        user_companies_len = 3

        user_data = get_user_data(user_id)

        assert_user(actual_user=user_data, user_id=user_id,
                    user_name=user_name, user_companies_len=user_companies_len)


    def test_get_user_id_2(self):
        print(f'Set was started, value = {self.random_value}')

        user_id = 2
        user_name = 'Ivan'
        user_companies_len = 2

        user_data = get_user_data(user_id)

        assert_user(actual_user=user_data, user_id=user_id,
                    user_name=user_name, user_companies_len=user_companies_len)



if __name__ == '__main__':
    unittest.main(verbosity=2)