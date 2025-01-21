from datetime import datetime, timedelta
import pytz
import time


# 1) зі строки server_time будемо створювати datetime object і вкажемо, що timezone = UTC
server_time = '2025-01-21 18:03:54.299397'
server_time_dt = datetime.fromisoformat(server_time)
server_time_dt_with_tz = pytz.timezone('UTC').localize(server_time_dt)  # пертворюемо в dt obj + відомості, що це UTC

# 2) перетвоюемо client_time в datime obj + додаємо відомості, що це в локальній timezone
client_time = '2025-01-21 19:03:55.399397'
client_time_dt = datetime.fromisoformat(server_time)  # об'єкт datetime без інформації про tz
local_tz = time.localtime().tm_zone  # поточна timezone
client_time_dt_with_tz = pytz.timezone(local_tz).localize(server_time_dt)  # пертворюемо в dt obj + відомості, що це UTC


current_dt = pytz.timezone(local_tz).localize(datetime.now())

diff = current_dt - server_time_dt_with_tz
# print(diff)
# print(diff.seconds)

def get_diff_between_dates_in_days(dt_1, dt_2):
    return (max([dt_1, dt_2]) - min([dt_2, dt_1])).days +  (max([dt_1, dt_2]) - min([dt_2, dt_1])).seconds /(60*60*24)

def get_diff_between_dates_in_hours(dt_1, dt_2):
    return  (max([dt_1, dt_2]) - min([dt_2, dt_1])).seconds /(60*60)

# print(get_diff_between_dates_in_hours(current_dt, server_time_dt_with_tz))
# print(get_diff_between_dates_in_hours(server_time_dt_with_tz, current_dt))


now_dt = datetime.now()
seven_day_ago = now_dt - timedelta(days=7)# , hours=8, seconds=20, minutes=99)
some_day_ago = now_dt + timedelta(days=-7, hours=8, seconds=20, minutes=99)
# print(now_dt - seven_day_ago)
# print(get_diff_between_dates_in_days(some_day_ago, now_dt))
# print(get_diff_between_dates_in_hours(seven_day_ago, now_dt))


# Перевірка роботи
time_a = datetime.now()  # отримаємо поточний час
time.sleep(3.5)
time_b = datetime.now()


if (time_b - time_a) > timedelta(seconds=3):
   print("WARNING! Різниця більше 3 секунд!")