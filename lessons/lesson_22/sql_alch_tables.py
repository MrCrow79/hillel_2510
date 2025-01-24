from sqlalchemy import create_engine, select, desc, asc, func, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from faker import Faker
import time

from sqlalchemy.orm import sessionmaker
from core.db_service.orm.tables.orm_dep import Department
from core.db_service.orm.tables.orm_emp import Employee
from core.db_service.orm.tables.sql_base import Base
from utils import db_connection_str

local_faker = Faker()

# З'єднання з базою даних PostgreSQL
# Потрібно вказати правильні дані для вашої бази даних
# DATABASE_URL = "postgresql://username:password@localhost:port/dbname"  # connection string


engine = create_engine(db_connection_str)

Base.metadata.create_all(engine)  # стврю таблиці


# Створюємо об'єкт сесії
Session = sessionmaker(bind=engine)
session = Session()

it_department = Department(name='IT')
hr_department = Department(name='HR')

john = Employee(name='John', department=it_department)
alice = Employee(name='Alice', department=hr_department)
bob = Employee(name='Bob', department=it_department)

session.add_all([it_department, hr_department, john, alice, bob])
session.commit()

# Вибірка співробітників та їх департаментів
employees = session.query(Employee).all()
for employee in employees:
    print(f"Ім'я: {employee.name}, Департамент: {employee.department.name}")

# Закриття сесії
session.close()

