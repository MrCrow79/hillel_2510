import psycopg2
import time

time.sleep(3)

conn = psycopg2.connect(
    dbname="postgres",
    user="anna",
    password="anna",
    host="localhost",
    port=5434
)