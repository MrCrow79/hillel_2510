from sqlalchemy import Column, Integer, String

from core.db_service.orm.tables.sql_base import Base


# Визначення моделі даних (таблиці) за допомогою класу
class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)


    def __str__(self):
        return f'products: id={self.id}, name={self.name}, price={self.price}'