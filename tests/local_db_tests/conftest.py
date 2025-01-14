import psycopg2
import pytest

dbname = 'new_db'
user = 'den'
password = 'den'
host = 'localhost'
port = '5432'


@pytest.fixture
def cursor():
    connection = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )
    cursor = connection.cursor()
    yield cursor

    if connection:
        connection.commit()

    if cursor:
        cursor.close()

    if connection:
        connection.close()