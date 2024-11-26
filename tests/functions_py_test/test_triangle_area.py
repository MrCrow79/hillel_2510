import pytest

from functions import triangle_area


@pytest.mark.positive
@pytest.mark.triangle_area
class TestTriangleArea:

    # @pytest.mark.xfail() - погана ідея
    @pytest.mark.parametrize('expected_result, triangles_numbers', [
        pytest.param(0.1, [0, 0, 0], marks=pytest.mark.xfail(reason='Knows issue: jira_link')),
        (0.133, [1, 1, 1]),
        (10.825, [5, 5, 5]),
        (432147.110, [999, 999, 999]),
    ], ids=['res = 0.1','res = 0.133', 'res = 10.825', 'res = 432147.110'])
    def test_triangle_area_positive(self, expected_result, triangles_numbers):

        # # не дуже гарний варіант
        # if expected_result == 0.1:
        #     pytest.xfail('Knows issue: jira_link')

        actual_result = round(triangle_area(*triangles_numbers), 3)

        assert actual_result == expected_result

    # def test_triangle_area_positive_1_1_1(self):
    #     expected_result = 0.433
    #     actual_result = round(triangle_area(1, 1, 1), 3)
    #
    #     assert actual_result == expected_result
    #
    # def test_triangle_area_positive_5_5_5(self):
    #     expected_result =  10.825
    #     actual_result = round(triangle_area(5, 5, 5), 3)  # обмежить число до 3 знаків після коми
    #
    #     assert actual_result == expected_result
    #
    # def test_triangle_area_positive_999(self):
    #     expected_result = 432147.110
    #     actual_result = round(triangle_area(999, 999, 999), 3)
    #
    #     assert actual_result == expected_result
