
FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1

RUN mkdir /app

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

WORKDIR /app/testEx
# Устанавливаем переменную окружения для Django
ENV DJANGO_SETTINGS_MODULE=testEx.settings

# Открываем порт, который будет использоваться приложением
EXPOSE 8000

RUN python manage.py collectstatic --noinput

CMD ["/app/.venv/Scripts/activate"]

CMD ["python", "manage.py", "makemigrations", "users", "tasks"]
CMD ["python", "manage.py", "migrate"]
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "testEx.wsgi:application"]