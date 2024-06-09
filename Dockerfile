
FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1

RUN mkdir /app

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

WORKDIR /app/testEx


RUN python manage.py collectstatic --noinput

CMD ["/app/.venv/Scripts/activate"]


CMD ["gunicorn", "--bind", "0.0.0.0:8000", "testEx.wsgi:application"]