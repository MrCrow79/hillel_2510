import pytest

from tests.ui_tests.positive_cases import PositiveCases


@pytest.mark.parametrize('user_id, expected_name', PositiveCases.data)
def test_check_user_names(user_id, expected_name):

    data = 'alex' # do some requests

    assert expected_name == data, f'for user_id {user_id} expected {expected_name} but got alex'