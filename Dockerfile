FROM python:3.11-slim

ENV PYTHONBUFFERED True

WORKDIR /flask-app
COPY . /flask-app/

RUN pip install --no-cache-dir -r requirements.txt

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app