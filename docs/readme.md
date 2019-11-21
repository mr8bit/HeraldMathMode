## Документация по работе с ботом

1. [Документация по API](/docs/bot/readme.md)
2. Работа бота
3. [Production](#Production)


##### Production
Для вывода в прод версию, необходиом установить Docker.

Для запуска должен быть создан в корне папки `.env` файл в который прописаны следующие переменные

```dockerfile
DJANGO_SETTINGS_MODULE - настройки для бота в прод версии
WEBHOOK_SITE - домен к которому привязан бот

TELEGRAM_TOKEN - токен телеграмм бота

CONFIRMATION_TOKEN - токен подтверждения ответа сервера ВК
API_TOKEN - токен для бота ВК

VIBER_AUTH_TOKEN - токен для ВК

VERIFY_TOKEN - токен верефикации для ФБ
ACCESS_TOKEN - токен доступа ФБ
```

После чего можно поднять при помощи команды     `docker-compose up --build`