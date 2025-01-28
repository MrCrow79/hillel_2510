from core.api_services.local_server.local_server_ctrl import LocalServer
import pytest


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


@pytest.fixture(scope='session')
def auth_header(local_server_ctrl):
    return local_server_ctrl.auth(json={"name": "test", "password": "test"}).text

