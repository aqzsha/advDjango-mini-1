# Используем официальный Python образ
FROM python:3.11

# Устанавливаем зависимости
RUN apt-get update && apt-get install -y netcat

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы проекта
COPY . .

# Устанавливаем зависимости проекта
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Ждём, пока БД будет доступна
CMD ["./wait-for-it.sh", "db:5432", "--", "python", "manage.py", "migrate"]

# Запуск Django-сервера
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "sales_trading.wsgi:application"]
