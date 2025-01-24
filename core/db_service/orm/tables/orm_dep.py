from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from core.db_service.orm.tables.sql_base import Base


# Визначення моделі даних (таблиці) за допомогою класу
class Department(Base):
    __tablename__ = 'departments'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    # Встановлення відношення "один до багатьох" з таблицею Employee
    employees = relationship("Employee", back_populates="department")


    def __str__(self):
        return f'Department: id={self.id}, name={self.name}'