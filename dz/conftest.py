import pytest
import psycopg2
from faker import Faker
import random
import os

dbname = os.getenv("POSTGRES_DB", "postgres")
user = os.getenv("POSTGRES_USER", "anna")
password = os.getenv("POSTGRES_PASSWORD", "anna")
host = os.getenv("DB_HOST", "db")  # "db" - це ім'я сервісу в docker-compose.yml
port = os.getenv("DB_PORT", "5432")


@pytest.fixture
def random_name():
    fake = Faker()
    return fake.first_name()


@pytest.fixture
def random_age():
    return random.randint(20, 70)


@pytest.fixture
def random_department():
    departments = ['hr', 'development', 'marketing', 'operations', 'support']
    return random.choice(departments)


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