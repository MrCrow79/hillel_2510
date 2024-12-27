import time
import random
from lessons.lesson_18.decorators_part_2 import retry

def wait_for_response(time_sec):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            res = func(*args, **kwargs)
            end_time = time.time()
            diff = end_time - start_time

            if diff < time_sec:
                print(f'waiting for {time_sec - diff} sec')
                time.sleep(time_sec - diff)

            print(f'Execution_time = {time.time() - start_time}')
            return res
        return wrapper
    return decorator

@retry(max_retries=2, delay=1)
@wait_for_response(8)
def send_request_to_server():
    start_time = time.time()
    sleep_sec = random.choice(range(1,5))
    if sleep_sec >= 2:
        raise TimeoutError()
    time.sleep(random.choice(range(1,5)))  # спати від 1 до 4 секунд

    print(f'fn inside {time.time() - start_time}')

start_time_of_ex = time.time()
send_request_to_server()
send_request_to_server()
send_request_to_server()
print(f'Real time of execution is {time.time() - start_time_of_ex}')