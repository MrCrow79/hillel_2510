from assertpy import soft_assertions
import pytest
from core.ui.sausedemo.asserts.product_page_asserts import check_prices_have_correct_format, assert_prices_are_sorter, \
    assert_names_are_sorter, assert_elements_are_sorter


from core.ui.sausedemo.helpers.product_page_helpers import get_values_from_product_pages


@pytest.mark.parametrize('sort_value, sort_type, is_price', [
    ('az', False, False),
    ('za', True, False),
    ('lohi', False, True),
    ('hilo', True, True),
], ids=['sort name asc', 'sort name desc', 'sort price asc', 'sort price desc',])
def test_sorting(product_page, sort_value, sort_type, is_price):

    product_page.product_page_check_page_is_opened()
    product_page.sort_by_value(value=sort_value)

    values = get_values_from_product_pages(product_page, is_price)
    assert_elements_are_sorter(elements=values, reverse=sort_type, is_price=is_price)




@pytest.mark.parametrize('sort_value, sort_type', [
    ('az', False),
    ('za', True)
], ids=['sort asc', 'sort desc'])
def test_sorting_name(product_page, sort_value, sort_type):

    product_page.product_page_check_page_is_opened()
    product_page.sort_by_value(value=sort_value)
    assert_names_are_sorter(names=product_page.get_all_names(), reverse=sort_type)


def test_sorting_price(product_page):

    product_page.product_page_check_page_is_opened()

    product_page.sort_by_price_asc()
    asc_prices = product_page.get_all_prices()

    product_page.sort_by_price_desc()
    desc_prices = product_page.get_all_prices()

    with soft_assertions():
        assert_prices_are_sorter(asc_prices, reverse=False)
        assert_prices_are_sorter(desc_prices, reverse=True)
