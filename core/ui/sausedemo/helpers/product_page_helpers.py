from core.ui.sausedemo.pages.product_page import ProductsPage


def get_values_from_product_pages(product_page: ProductsPage, is_price: bool):

    if is_price:
        return product_page.get_all_prices()

    return product_page.get_all_names()