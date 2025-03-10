# Використовуємо офіційний образ Python версії 3.9
FROM python:3.9

# Копіюємо файли з локальної директорії в контейнер
COPY .. /app

# Задаємо робочу директорію контейнера
WORKDIR /app

# Встановлюємо залежності для тестування
RUN pip install -r requirements.txt

# Виконуємо команду для запуску тестів під час створення контейнера
CMD ["pytest", "tests", "-m", "triangle_area"]