from setting import d_settings
from core.api_services.local_server.local_server_ctrl import LocalServer
import time
import pytest
import os

from utils import BASE_DIR


# scopes:
# session - 1 раз за всі тести за запуск
# package - 1 раз за всі тести в папці
# module - 1 раз за всі тести в файлі
# class - 1 раз за всі тести в класі
# function - при кожному тесті тести, default
@pytest.fixture(scope='session')  # запускаеться 1 раз для всіх тестів
def local_server_ctrl():
    print('RUNNING FIXTURE local_server_ctrl')
    ctrl = LocalServer()
    return ctrl


@pytest.fixture(scope='session')  # autouse=False by default
def auth_header(local_server_ctrl):
    return local_server_ctrl.auth(json={"name": "test", "password": "test"}).text


@pytest.fixture(scope='session', autouse=True)
def time_logging():
    print('STARTING time_logging')
    start_time = time.time()
    yield
    print(f'Tests execution time is {time.time() - start_time}')


@pytest.fixture(scope='session', autouse=bool(int(d_settings.delete_logs_after_tests)))
def deleting_pytest_logs_files():
    yield
    for dirname, subdirs, files in os.walk(BASE_DIR):
        if 'pytest_logs.log' in files:
            full_path = os.path.join(dirname, 'pytest_logs.log')
            print(f'Deleting {full_path}')
            os.remove(full_path)





