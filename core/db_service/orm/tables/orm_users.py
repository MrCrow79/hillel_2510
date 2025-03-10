from sqlalchemy import Column, Integer, String

from core.db_service.orm.tables.sql_base import Base


# Визначення моделі даних (таблиці) за допомогою класу
class ORMUser(Base):
    __tablename__ = 'orm_users'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    age = Column(Integer)


    def __str__(self):
        return f'id={self.id}, name={self.name}, age={self.age}'