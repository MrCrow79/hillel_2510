from datetime import datetime
import pytz
import time

# client_time = '2025-01-21 19:03:55.399397'
# server_time = '2025-01-21 18:03:54.299397'  # час який витягнув з БД, якщо не вказана timezone, то це UTC
#
# server_time_dt = datetime.fromisoformat(server_time)  # UTC
#
#
# client_time_dt = datetime.fromisoformat(client_time)  # UTC
#
# current_tz = time.localtime().tm_zone
#
# client_time_dt = pytz.timezone(current_tz).localize(client_time_dt)
#
#
#
# current_time = pytz.timezone(current_tz).localize(datetime.now())
# print(datetime.now())
# print(current_time)

# '2025-01-21 18:03:54.299397'  -  час в UTC, бо не вказана timezone

# 1) зі строки server_time будемо створювати datetime object і вкажемо, що timezone = UTC
server_time = '2025-01-21 18:03:54.299397'
server_time_dt = datetime.fromisoformat(server_time)
server_time_dt_with_tz = pytz.timezone('UTC').localize(server_time_dt)  # пертворюемо в dt obj + відомості, що це UTC

# 2) перетвоюемо client_time в datime obj + додаємо відомості, що це в локальній timezone
client_time = '2025-01-21 19:03:55.399397'
client_time_dt = datetime.fromisoformat(server_time)  # об'єкт datetime без інформації про tz
local_tz = time.localtime().tm_zone  # поточна timezone
client_time_dt_with_tz = pytz.timezone(local_tz).localize(server_time_dt)  # пертворюемо в dt obj + відомості, що це UTC


print(server_time_dt - client_time_dt)
print(server_time_dt_with_tz - client_time_dt_with_tz)

def get_datetime_from_isoformat_in_utc_dt(time_str):
    time_str = datetime.fromisoformat(time_str)
    return pytz.timezone('UTC').localize(time_str)