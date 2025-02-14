from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from core.ui.sausedemo.product_page_locators import ProductPageLocators
from setting import d_settings


from core.ui.sausedemo.pages.base_page import BasePage
from setting import d_settings


class ProductsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver=driver, url=f"{d_settings.sauserdemo_url}inventory.html")


    def product_page_check_page_is_opened(self, timeout=1):

        # url який я очікую від сторінки ProductsPage
        assert self._driver.current_url == self.url, f"Url of products page should be {self.url}"

        self._element_present(locator=ProductPageLocators.product_item, timeout=timeout,
                                     message='Cant find any product block on products page')