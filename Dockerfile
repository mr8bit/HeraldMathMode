# сборка фронтенда
FROM node:lts-alpine as frotnend-stage
# создаем рабочую папку
WORKDIR /usr/app/src
# копируем все для сборки
COPY package*.json ./
COPY vue.config.js ./
COPY ./src .
# запускаем установку зависимостей
RUN npm install --production
# запускаем сборку фронта
RUN npm run build

# Сборка backend части
FROM python:3.6.8 as backend-stage
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE backend.settings.prod
# создаем рабочую папку
WORKDIR /usr/app
# копируем рабочие файлы
COPY ./backend ./backend
COPY ./requirements.txt .
COPY ./manage.py .
# создаем зависимости
RUN pip install Cython==0.29.3 cysignals==1.9.0
RUN pip install -r requirements.txt






