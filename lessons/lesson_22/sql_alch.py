from sqlalchemy import create_engine, select, desc, asc, func, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from faker import Faker
import time

from sqlalchemy.orm import sessionmaker
from core.db_service.orm.tables.orm_users import ORMUser
from core.db_service.orm.tables.sql_base import Base
from setting import d_settings
from chrom_utils import db_connection_str

local_faker = Faker()

# З'єднання з базою даних PostgreSQL
# Потрібно вказати правильні дані для вашої бази даних
# DATABASE_URL = "postgresql://username:password@localhost:port/dbname"  # connection string


engine = create_engine(db_connection_str)

Base.metadata.create_all(engine)  # стврю таблиці


# Створюємо об'єкт сесії
Session = sessionmaker(bind=engine)
session = Session()

# Додавання нового користувача
new_user = ORMUser(name=local_faker.name(), age=30)
session.add(new_user)
session.commit()

users = [ORMUser(name=local_faker.name(), age=31) for _ in range(5)]

session.add_all(users)
session.commit()

# Відповідає INSERT INTO users (name, age) VALUES ('John', 30);
#
# Оновлення інформації про користувача
# filters = {"age": 30, "name": "Patrick Warren"}
# users = session.query(ORMUser).filter_by(**filters).all()
# users = session.query(ORMUser).filter_by(age=30, name="Patrick Warren").all()
#
# print(*users, sep='\n')

# select_user_query = select(ORMUser).where(ORMUser.age > 30)  #  сформую запит
# # session.execute(select_user_query) - повертає список таблів
# users = [k[0] for k in session.execute(select_user_query)]  # беремо перший елемент кожного таплу із відповіді
# # print(*users, sep='\n')
#
# user_with_age_31 = session.query(ORMUser).filter_by(age=31).first()
#
# user_with_age_31.name = f'Vlad-{time.time()}'
# user_with_age_31.age = 100
# session.commit()
# print(*session.query(ORMUser).filter_by(age=100).all())
#
#
# for user in session.query(ORMUser).filter_by(age=31).all():
#     user.age = 35
#
# session.commit()
# print(*session.query(ORMUser).filter_by(age=35).all(), sep='\n')


# user.age = 31
# session.commit()
# # Відповідає UPDATE users SET age=31 WHERE name='John';
#
# Видалення користувача

# user = session.query(ORMUser).first()
#
# print(user)

# session.delete(user)
# session.commit()
# Відповідає DELETE FROM users WHERE name='John';
#

print(session.query(func.avg(ORMUser.id)).scalar())
print(*session.query(ORMUser).all(), sep='\n')


print('-'*80)
print(d_settings.USER_NAME)

# select COUNT(id) from ....
# select AVG(age) from ...


# print(session.query(ORMUser).order_by(asc(ORMUser.id)).first())