# Сборка backend части
FROM python:3.7.3-alpine
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE backend.settings.prod
# создаем рабочую папку
WORKDIR /usr/src/app
# копируем рабочие файлы
COPY ./backend ./backend
COPY ./requirements.txt .
COPY ./uwsgi.ini .
COPY ./entrypoint.sh .
COPY ./manage.py .
# создаем зависимости
RUN apk update && apk add git libressl-dev postgresql-dev libffi-dev gcc musl-dev python3-dev
RUN pip install -r requirements.txt
RUN pip install raven
RUN pip install uwsgi
RUN pip install psycopg2
RUN pip install gunicorn
RUN ls -l







