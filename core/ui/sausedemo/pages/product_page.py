from core.ui.sausedemo.locators.product_page_locators import ProductPageLocators
from selenium.webdriver.support.select import Select

from core.ui.sausedemo.pages.base_page import BasePage
from setting import d_settings
import allure


class ProductsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver=driver, url=f"{d_settings.sauserdemo_url}inventory.html")

    @allure.step('Product_page: checking page is opened')
    def product_page_check_page_is_opened(self, timeout=1):
        # url який я очікую від сторінки ProductsPage
        allure.step('Product_page: checking page url')
        assert self._driver.current_url == self.url, f"Url of products page should be {self.url}"

        allure.step('Product_page: checking page product block')
        self._element_present(locator=ProductPageLocators.product_item, timeout=timeout,
                              message='Cant find any product block on products page')

    @allure.step('Product_page: getting all prices')
    def get_all_prices(self, timeout=1):

        prices_els = self._elements_present(locator=ProductPageLocators.product_price, timeout=timeout,
                                                  message='Cant find any prices block on products page')
        return [k.text for k in prices_els]

    @allure.step('Product_page: getting all names')
    def get_all_names(self, timeout=1):

        prices_els = self._elements_present(locator=ProductPageLocators.product_name, timeout=timeout,
                                                  message='Cant find any prices block on products page')
        return [k.text for k in prices_els]

    def sort_by_name_asc(self, timeout=1):
        return self.sort_by_value(value='az', timeout=timeout)

    def sort_by_name_desc(self, timeout=1):
        return self.sort_by_value(value='za', timeout=timeout)

    def sort_by_price_asc(self, timeout=1):
        return self.sort_by_value(value='lohi', timeout=timeout)

    def sort_by_price_desc(self, timeout=1):
        return self.sort_by_value(value='hilo', timeout=timeout)


    @allure.step('Product_page sorting: {value}')
    def sort_by_value(self, value: str, timeout=1):

        sorting_dropdown = Select(self._element_present(locator=ProductPageLocators.sorting_dropdown, timeout=timeout,
                                                  message='Cant sorting_dropdown'))
        sorting_dropdown.select_by_value(value)

        return self



######### checks
    def check_n_products_on_a_page(self, timeout=1, expected_products: int = None):
        return self.__check_n_elements(timeout=timeout,
                                       expected_elements=expected_products,
                                       locator=ProductPageLocators.product_item)

    def check_n_prices_on_a_page(self, timeout=1, expected_prices: int = None):
        return self.__check_n_elements(timeout=timeout,
                                       expected_elements=expected_prices,
                                       locator=ProductPageLocators.product_price)

    def __check_n_elements(self, expected_elements, locator, timeout=1):
        if expected_elements is None:
            self.logger.info(f'Checking {expected_elements} elements ')
            expected_elements = int(d_settings.sauserdemo_number_products_on_a_page)

        self.get_n_elements_presents(locator=locator, quantity_of_elements=expected_elements,
                                     timeout=timeout, message=f'Check {expected_elements} on the products page')

        return self
