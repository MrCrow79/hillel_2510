from core.api_services.local_server_ctrl import LocalServer
import pytest



@pytest.fixture(scope='session')  # запускаеться 1 раз для всіх тестів
def local_server_ctrl():
    print('RUNNING FIXTURE local_server_ctrl')
    ctrl = LocalServer()
    return ctrl