
from selenium.webdriver.common.by import By


class ProductPageLocators:

    container_of_elements = (By.XPATH, '//div[@class="header_secondary_container"]')
    product_item = (By.XPATH, '//div[@data-test="inventory-item-description"]')
    product_price = (By.XPATH, '//div[@data-test="inventory-item-price"]')
    product_name = (By.XPATH, '//div[@data-test="inventory-item-name"]')
    sorting_dropdown = (By.XPATH, '//select[@data-test="product-sort-container"]')