import os
import unittest
import pytest


current_env = os.getenv('CUR_ENV', 'dev')

class BaseTest(unittest.TestCase):

    @pytest.mark.positive
    def test_base_assert(self):
        expected_result = 10
        actual_result = 5 * 2
        self.assertEqual(actual_result, expected_result)  # assert expected_result == actual_result

    @pytest.mark.skipif(current_env == 'dev', reason='Cant be run on dev')
    def test_base_assert_failed(self):
        assert 1 == 2  # asseration error = failed, # assert condition, condition = bool value

    @pytest.mark.skip(reason='test example of failed test')  # pytest не буде запускати тест
    def test_base_assert_broken(self):
        raise AttributeError  # AttributeError error = broken


class ConditionTest(unittest.TestCase):

    @pytest.mark.xfail(reason='Unstable')
    def test_equal_true(self):
        assert True, 'Can\'t be failed'

    def test_equal_false(self):
        assert False, 'Failed always, because False'

    def test_equal_self_false(self):

        self.assertEqual(1, 2)

    @pytest.mark.xfail(reason='Unstable')
    def test_is_self_false(self):
        expected = [1,2]
        actual = [1,2]
        self.assertIs(expected, actual)

        # a == b, значить порівнювати значення
        # a is b, значить порівнювати адреси в пам'яті двоз об'єктів, тобто id(a) == id(b)

    def test_almost_equal_self_false(self):
        self.assertAlmostEqual(1, 5, delta=3)




if __name__ == '__main__':
    unittest.main(verbosity=2)
