
from selenium.webdriver.common.by import By


class ProductPageLocators:

    container_of_elements = (By.XPATH, '//div[@class="header_secondary_container"]')
    product_item = (By.XPATH, '//div[@data-test="inventory-item-description"]')