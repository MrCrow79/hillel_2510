
from functions import factorial  # from шлях_до_файла_з_початку_проекта import фунція_з_файла
import pytest


@pytest.mark.positive
@pytest.mark.factorial_custom
def test_factorial_positive_simple():
    expected_result = 120
    actual_result = factorial(5)

    assert actual_result == expected_result

