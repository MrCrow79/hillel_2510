import time
import random


# print(time.time())  # повертае число, або його називають timestamp

# print(time.localtime())  # об'єкт
# print(f'hour is {time.localtime().tm_hour}')
# print(f'min is {time.localtime().tm_min}')
# print(f'year is {time.localtime().tm_year}')
# print(f'tz name is {time.localtime().tm_zone}')


# print(time.localtime())
# time.sleep(3.5)  #  чекати 3.5 секунди
# print(time.localtime())

start_time = time.time()  # зараз
max_time_wait = 20  # sec

# while time.time() - start_time < max_time_wait:  # чекати максимум 20 секунд
#     """Ми друкуемо Waiting кону секунду на протязі 20 секунд"""
#     print('Waiting ....')
#     time.sleep(1)

def get_response_status_code_from_server():
    res = random.choice(range(20))  # випадково обере число від 0 до 19

    if res < 5:
        return  200
    else:
        return 400

if __name__ == '__main__':
    is_response_ok = False
    while time.time() - start_time < max_time_wait:  # чекати максимум 20 секунд

        result = get_response_status_code_from_server()  # роблю запит на сервер
        print('Waiting ....')
        print(f'status code of response is {result}')
        if result == 200:
            is_response_ok = True
            break
        time.sleep(1)

    assert is_response_ok is True, f'Response doesnt return status code 200 for {max_time_wait} seconds'