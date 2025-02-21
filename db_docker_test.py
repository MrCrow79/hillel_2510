import psycopg2

import time
import os
#
# from setting import d_settings
#
# conn = psycopg2.connect(
#     dbname=d_settings.DB_NAME,
#     user=d_settings.DB_USER,
#     password=d_settings.DB_PASS,
#     host=d_settings.DB_HOST,
#     port=d_settings.DB_PORT
# )


time.sleep(2)

conn = psycopg2.connect(
    dbname=os.getenv('DB_NAME'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT')
)