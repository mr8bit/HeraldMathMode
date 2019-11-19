# сборка фронтенда
FROM node:8.16-alpine as frotnend-stage
# создаем рабочую папку
WORKDIR /usr/app
# копируем все для сборки
COPY package*.json ./
COPY vue.config.js ./
COPY ./src ./src
# запускаем установку зависимостей
RUN npm install
# запускаем сборку фронта
RUN npm run build

# Сборка backend части
FROM python:3.6.9-alpine3.9 as backend-stage
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE backend.settings.prod
# создаем рабочую папку
WORKDIR /usr/app
# копируем рабочие файлы
COPY ./backend ./backend
COPY ./requirements.txt .
COPY ./entrypoint.sh .
COPY ./manage.py .
# создаем зависимости
RUN apk update && apk add git libressl-dev postgresql-dev libffi-dev gcc musl-dev python3-dev
RUN pip install -r requirements.txt
RUN pip install gunicorn
RUN ls -l

ENTRYPOINT ["/bin/sh", "entrypoint.sh"]






