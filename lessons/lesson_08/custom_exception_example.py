class AgeError(Exception):

    def __init__(self, age):
        message = f'Incorrect age  {age}. Age must be NOT between 18 and 60'
        super().__init__(message)

class ProductHasNoDiscount(Exception):

    def __init__(self):
        super().__init__('Your product not has no discount')


def get_discount(user_age, product_id):
    discount_products = [1,2,10, 50]

    if 18 < user_age < 60:
        raise AgeError(user_age)

    if product_id not in discount_products:
        raise ProductHasNoDiscount()

    return 20  # 20 відсотків


get_discount(66, 100500)
