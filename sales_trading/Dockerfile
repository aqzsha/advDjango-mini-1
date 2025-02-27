FROM python:3.11-slim-buster

RUN apt-get update && apt-get install -y netcat
ENV PYTHONUNBUFFERED=1
WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# # Ждём, пока БД будет доступна
# CMD ["./wait-for-it.sh", "db:5432", "--", "python", "manage.py", "migrate"]

# # Запуск Django-сервера
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "sales_trading.wsgi:application"]
CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000"]