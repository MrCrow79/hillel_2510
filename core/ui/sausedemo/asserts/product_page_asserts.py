import re
from assertpy import assert_that, soft_assertions, soft_fail
from typing import List


def check_prices_have_correct_format(prices: List[str]):
    with soft_assertions():
        for price in prices:

            re_for_check_price = r'(\$\d+)(\.\d{1,2})?'
            error_message = f"Price has not expected format {price}"
            res = re.match(re_for_check_price, price)

            if not res:
                soft_fail(error_message)
                continue
            res = res.groups()
            found_price = ''.join(res)

            assert_that(found_price).is_equal_to(price)
            assert_that(found_price).contains_duplicates()



def assert_prices_are_sorter(prices, reverse: bool):

    prices = [float(k[1:]) for k in prices]
    assert_that(prices).is_sorted(reverse=reverse)


def assert_names_are_sorter(names, reverse: bool):
    assert_that(names).is_sorted(reverse=reverse)


def assert_elements_are_sorter(elements: list, reverse: bool, is_price: bool):

    if is_price:
        elements = [float(k[1:]) for k in elements]
    assert_that(elements).is_sorted(reverse=reverse)

