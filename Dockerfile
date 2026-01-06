# Берём официальный Python образ
FROM python:3.11-alpine3.16

# Отключаем .pyc и буферизацию
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Рабочая директория внутри контейнера
WORKDIR /app

# Копируем requirements
COPY requirements.txt /app/requirements.txt
COPY . /app

# Системные зависимости (для psycopg2, pillow)
RUN apk add --no-cache postgresql-client build-base postgresql-dev && \
    pip3 install -r requirements.txt

# Копируем весь проект
COPY . .

# Открываем порт
EXPOSE 8000

# Команда запуска
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]