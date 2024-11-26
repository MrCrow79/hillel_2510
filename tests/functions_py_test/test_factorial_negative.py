import pytest

from functions import factorial  # from шлях_до_файла_з_початку_проекта import фунція_з_файла
from tests.basic_tests.test_basic import current_env


@pytest.mark.negative
@pytest.mark.factorial_custom
def test_factorial_negative():

    with pytest.raises(TypeError):
        factorial('5')


@pytest.mark.negative
@pytest.mark.factorial_custom
def test_factorial_without_catching():

    try:
        result = factorial(-3)
    except ValueError:

        # if current_env == 'dev':
        pytest.skip('Fix test because new requirements')  # TODO)
    expected = 0

    assert result == expected


@pytest.mark.negative
@pytest.mark.factorial_custom
def test_factorial_fail():

    pytest.fail('Always fail')
    factorial(-3)


