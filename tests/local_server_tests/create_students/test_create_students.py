import pytest
import time
import pytz
from datetime import datetime, timedelta


@pytest.mark.smoke
@pytest.mark.local_server
@pytest.mark.parametrize('user_id', [1,2])
@pytest.mark.parametrize('user_name', ['den', 'ivan'])
def test_create_students(local_server_ctrl, user_name, auth_header, user_id):

    print(f'run for user_id, user_name {user_id}={user_name}')
    local_server_ctrl.create_student(json={"name": "Alex", "score": 50}, auth_data=auth_header)


def test_create_students_with_max_score(local_server_ctrl, body_user_with_max_score, auth_header):

    local_server_ctrl.create_student(json=body_user_with_max_score, auth_data=auth_header)


@pytest.mark.local_server
def test_create_students_check_datetime_fields(local_server_ctrl, auth_header):

    time_start = datetime.now()  # час старту тесту, де я НЕ відправив запит на створення юзера

    resp = local_server_ctrl.create_student(json={"name": "Alex", "score": 50}, auth_data=auth_header).json()

    time_finish = datetime.now()  #  час продовження тестау, де юзер ВЖЕ створенний

    # assert_time_fileds_user_was_created(resp, time_start, time_finish)

    # 1)  created_date -> datetime obj as UTC, time_finish -> dt obj with local TZ -> comparing
    # 2)  updated_date -> datetime obj as TZ from updated_date, time_finish -> dt obj with local TZ -> comparing

    user_created_date = resp['created_date']  # timestamp time.time()

    # 1) зробимо з timestamp об'єкт datetime вказуючі, що tz повинна бути UTC
    user_created_date_utc_dt = datetime.fromtimestamp(user_created_date, tz=pytz.UTC)

    # 2) перетворюемо time_finish в datatime об'єкт
    time_finish_tz_dt = pytz.timezone(time.localtime().tm_zone).localize(time_finish)

    #3) ми отримаємо різницю між  time_start i time_finish
    delta = time_finish - time_start


    print(f'user_created_date_utc_dt is {user_created_date_utc_dt}')
    print(f'time_finish_tz_dt is {time_finish_tz_dt}')
    print(f'delta is {delta}')
    print(f'time_finish_tz_dt - user_created_date_utc_dt is {time_finish_tz_dt - user_created_date_utc_dt}')

    # 4) порівню'ємо

    min_value = min([time_finish_tz_dt, user_created_date_utc_dt])
    max_value = max([time_finish_tz_dt, user_created_date_utc_dt])
    assert (max_value - min_value) < delta, \
        f'Expected created_date between {time_finish_tz_dt} +- {delta}, but actual is {user_created_date_utc_dt}'

    user_updated_date = datetime.strptime(resp['updated_date'], '%Y-%m-%dT%H:%M:%S%z')

    min_value = min([user_created_date_utc_dt, user_updated_date])
    max_value = max([user_created_date_utc_dt, user_updated_date])

    # порівняння того, що різниця між user_created_date_utc_dt та user_updated_date менше секунди
    assert (max_value - min_value) < timedelta(seconds=1)



    #user_updated_date = resp['updated_date']  # server local time

    # updated_date = 2025-01-21T21:05:27+0200'
