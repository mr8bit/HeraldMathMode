## API

API для управления и получения информации о состоянии бота.

Список запросов:
- Авторизация 
- [Оповещения](#Оповещения)
- FAQ
- [Помощь](#Помощь)
    - Ответ пользователю 
- [Статистика](#Статистика)
    - [Статистика запросов](#Список-запросов)
    - [По состояниям](#Сгруппированный-по-состояниям)

---
#### Авторизация
Авторизация построена на основе [django-rest-framework-simplejwt](https://github.com/davesque/django-rest-framework-simplejwt)

Для получения токена, достаточно передать логин с паролем
```shell script
curl \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "admin"}' \
  http://localhost:8000/api/token/
```

А в ответ приедет токен авторизации и токен для обновления: 
```json
{
  "access":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjoxLCJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiY29sZF9zdHVmZiI6IuKYgyIsImV4cCI6MTIzNDU2LCJqdGkiOiJmZDJmOWQ1ZTFhN2M0MmU4OTQ5MzVlMzYyYmNhOGJjYSJ9.NHlztMGER7UADHZJlxNG0WSi22a2KaYSfd1S-AuT7lU",
  "refresh":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjoxLCJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImNvbGRfc3R1ZmYiOiLimIMiLCJleHAiOjIzNDU2NywianRpIjoiZGUxMmY0ZTY3MDY4NDI3ODg5ZjE1YWMyNzcwZGEwNTEifQ.aEoAYkSJjoWH1boshQAaTkf8G3yn0kapko6HFRt7Rh4"
}
```
Для получения доступа к защищенным элементам необходимо добавить в `Header` заголовок  `Authorization`

```shell script
curl \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjoxLCJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiY29sZF9zdHVmZiI6IuKYgyIsImV4cCI6MTIzNDU2LCJqdGkiOiJmZDJmOWQ1ZTFhN2M0MmU4OTQ5MzVlMzYyYmNhOGJjYSJ9.NHlztMGER7UADHZJlxNG0WSi22a2KaYSfd1S-AuT7lU" \
  http://localhost:8000/api/some-protected-view/
```

Когда токен закончит действовать, его необходимо обновить 
```shell script
curl \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{"refresh":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjoxLCJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImNvbGRfc3R1ZmYiOiLimIMiLCJleHAiOjIzNDU2NywianRpIjoiZGUxMmY0ZTY3MDY4NDI3ODg5ZjE1YWMyNzcwZGEwNTEifQ.aEoAYkSJjoWH1boshQAaTkf8G3yn0kapko6HFRt7Rh4"}' \
  http://localhost:8000/api/token/refresh/
```

После чего получите новый токен
```json
{"access":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjoxLCJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiY29sZF9zdHVmZiI6IuKYgyIsImV4cCI6MTIzNTY3LCJqdGkiOiJjNzE4ZTVkNjgzZWQ0NTQyYTU0NWJkM2VmMGI0ZGQ0ZSJ9.ekxRxgb9OKmHkfy-zs1Ro_xs1eMLXiR17dIDBVxeT-w"}
```
---
#### Оповещения

Метод позволяет получить список и создать оповещения как для всех месенджеров так и для определенного месенджера.

Получить все оповещения: 

```rest
GET
/api/notifications
```

Пример:
```json
[
    {
        "name": "Первое оповещение",
        "message": "Это мое первое оповещение",
        "for_messenger": 0
    },
    ...
]
```

Получить оповещение по id: 

```rest
GET
/api/notifications/<id>
```

Пример:
```json
{
        "name": "Первое оповещение",
        "message": "Это мое первое оповещение",
        "for_messenger": 0
}
```

Создать новое оповещение:
```rest
POST
/api/notifications
```
Пример: <br/>
`Media type: application/json`
```json
{
    "name": "Новое оповещение 2",
    "message": "Это мое второе оповещение",
    "for_messenger": 4
}
```

---

#### Помощь
Позволяет получить список жалоб пользователей.

```rest
GET
/api/help
```

Пример
```json
[
    {
        "id": 20,
        "user": "66489748",
        "message": "Он очень плохо работает",
        "date": "2019-11-20T21:43:36.164000Z",
        "category": "bot"
    },
    ...
]
```

Жалоба пользователя по Id

```rest
GET
/api/help/<:id>
```

```json
{
    "id": 1,
    "user": "66489748",
    "message": "Он очень плохо работает",
    "date": "2019-11-20T21:43:36.164000Z",
    "category": "bot"
}
```
##### Ответ пользователю
Позволяет отправить ответ на вопрос/жалобу пользователя
```rest
POST
/api/issues/answer
```

`Media type: application/json`
```json
{
    "issue": 1,
    "text": "Ответ на ваш вопрос"
}
```

---
#### Статистика
##### Список запросов
Позволяет получить статистику запросов к боту. 

За текущий месяц: 
```rest
GET 
/api/request/month
```

За текущий день: 
```rest
GET
/api/request/day
```

За текущую неделю: 
```rest
GET
/api/request/week
```

За промежуток: 
```rest
GET
/api/request/ranage/?start=01.11.2019&end=20.11.2019
```

Формат:
```json
[
  {
    "id": Уникальный номер,
    "user": Id пользователя,
    "state": Экран на котором был пользователь,
    "date": Дата запроса,
    "text": Текст запроса
  },
   ..
]
```

Пример: 
```json
 [
  {
    "id": 1,
    "user": "66489748",
    "state": "backend.schedule.states.main.MainMenu",
    "date": "2019-11-19",
    "text": "🔜Расписание на завтра"
  },
  ...
]
```
---
##### Сгруппированный по состояниям
Метод позволяет получить статистику 

За текущий месяц:
 ```rest
GET 
/api/request/groupby/state/month
```

За текущий день:
```rest
GET 
/api/request/groupby/state/day
```

За текущую неделю:
```rest
GET 
/api/request/groupby/state/week
```

За промежуток: 
```rest
GET
/api/request/groupby/state/ranage/?start=01.11.2019&end=20.11.2019
```

Формат:
```json
[
  {
        "state": Состояние,
        "dcount": Количество
   },
  ...
]
```
Пример: 
```json
[ 
  {
        "state": "backend.schedule.states.main.MainMenu",
        "dcount": 5
   },
    ...
]
```
---
