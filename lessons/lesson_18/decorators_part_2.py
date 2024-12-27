import time

def retry(max_retries, delay=1, error_type=Exception):
    def decorator(func):
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_retries:
                try:
                    # Спроба виклику функції, яку декоруємо
                    return func(*args, **kwargs)
                except error_type as e:
                    # Обробка помилки та вивід повідомлення про спробу
                    print(f"Помилка: {e}. Повторна спроба {retries + 1}/{max_retries}")
                    retries += 1
                time.sleep(delay)
            # Викидаємо виняток, якщо досягнуто максимальну кількість спроб
            raise error_type("Досягнуто максимальну кількість спроб")
        return wrapper
    return decorator


# @retry(max_retries=3, delay=2, error_type=ZeroDivisionError)
# def division(num1, num2):
#     print('division ...')
#     return num1/num2
#
# division(1, 0)