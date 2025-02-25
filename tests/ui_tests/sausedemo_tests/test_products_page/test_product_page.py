from core.ui.sausedemo.asserts.product_page_asserts import check_prices_have_correct_format

from time import sleep
import os

from utils import BASE_DIR, SCREENSHOTS


def test_n_products_on_a_page(product_page):

    product_page.product_page_check_page_is_opened()
    product_page.check_n_products_on_a_page()



def test_all_products_have_correct_price(product_page):

    product_page.product_page_check_page_is_opened()
    prices = product_page.get_all_prices()  # list of strings

    # assert correct type of prices
    check_prices_have_correct_format(prices)

    product_page._driver.maximize_window()
    product_page._driver.get_screenshot_as_file(os.path.join(SCREENSHOTS, 'test_all_products_have_correct_price.png'))



