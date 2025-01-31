import pytest
import sqlite3

import os

from core.api_services.local_server.local_server_ctrl import LocalServer
from setting import d_settings
from utils import BASE_DIR

DEFAULT_USERS_LIMIT = 10


@pytest.fixture(scope='session')
def db_cursor():
    connector = sqlite3.connect(os.path.join(BASE_DIR, d_settings.sqlite_path))
    cursor = connector.cursor()
    yield cursor
    cursor.close()
    connector.close()



@pytest.fixture()
def get_quantity_of_users(db_cursor):

    db_cursor.execute('select count(id) from student')

    return db_cursor.fetchone()[0]



def get_last_n_students():
    ctrl = LocalServer()
    return ctrl.get_students(params={'limit': 10, 'sort_by': '-id'}).json()

@pytest.fixture(scope='function', params=get_last_n_students())  # function == default scope
def last_n_students_parametrized(request):
    # num = random.choice(range(10))
    #
    # if num > 5:
    #     request.param.pop('created_date')

    if request.param['id'] in [555, 3570]:  # якщо student_id in [555, 3570]
        pytest.skip('Cant run test for id 555 and 3570')

    return request.param




def read_data_on_dev():
    pass


def read_data_on_stage():
    pass


def read_data_on_prod():
    pass

@pytest.fixture()
def read_data_depend_on_env():
    if d_settings.current_env == 'dev':
        return read_data_on_dev()
    if d_settings.current_env == 'stage':
        return read_data_on_stage()
    if d_settings.current_env == 'prod':
        return read_data_on_prod()