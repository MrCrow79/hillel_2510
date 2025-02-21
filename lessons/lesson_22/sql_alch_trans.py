from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.db_service.orm.tables.orm_products import Product
from core.db_service.orm.tables.sql_base import Base
from chrom_utils import PG_DATABASE_URL

local_faker = Faker()



engine = create_engine(PG_DATABASE_URL)
Base.metadata.create_all(engine)  # стврю таблиці


# Створюємо об'єкт сесії
Session = sessionmaker(bind=engine)
session = Session()

try:
    # Початок транзакції
    session.begin()

    # Додавання нового продукту
    new_product = Product(name='Laptop', price=1000)
    session.add(new_product)

    # Збільшення ціни для всіх продуктів на 10%
    session.query(Product).update({Product.price: Product.price * 1.1})

    raise AttributeError

    # Збільшення ціни для конкретного продукту на 5%
    product = session.query(Product).filter_by(name='Laptop').first()
    product.price *= 1.05

    # Підтвердження транзакції
    session.commit()
except Exception as e:
    # Скасування транзакції в разі виникнення помилки
    session.rollback()
    print(f'Smth went wrong {e}')
finally:
    session.close()


all_leptops = session.query(Product).filter_by(name='Laptop').all()

for l in all_leptops:
    l.name = 'Super discount for Laptop'
session.commit()