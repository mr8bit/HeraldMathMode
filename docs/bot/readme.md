## API

API для управления и получения информации о состоянии бота.

Список запросов:
- Статистика запросов
    - Список запросов
        - Месяц
        - Неделя
        - День
        - Промежуток
    - Сгруппированный по состояниям
        - Месяц
        - Неделя
        - День
        - Промежуток
        
     
#### Статистика запросов:
##### Список запросов
За текущий месяц: `GET /api/request/month`<br/>
За текущий день: `GET /api/request/day`<br/>
За текущую неделю: `GET /api/request/week`<br/>
За промежуток: `GET /api/request/ranage/?start=01.11.2019&end=20.11.2019`<br/>
Формат:
```rest
 {
        "id": Уникальный номер,
        "user": Id пользователя,
        "state": Экран на котором был пользователь,
        "date": Дата запроса,
        "text": Текст запроса
    },
```
Пример: 
```rest
 {
        "id": 1,
        "user": "66489748",
        "state": "backend.schedule.states.main.MainMenu",
        "date": "2019-11-19",
        "text": "🔜Расписание на завтра"
    },
```

##### Сгруппированный по состояниям
За текущий месяц: `GET /api/request/groupby/state/month`<br/>
За текущий день: `GET /api/request/groupby/state/day`<br/>
За текущую неделю: `GET /api/request/groupby/state/week`<br/>
За промежуток: `GET /api/request/groupby/state/ranage/?start=01.11.2019&end=20.11.2019`<br/>
Формат:
```rest
 {
        "state": Состояние,
        "dcount": Количество
    },
```
Пример: 
```rest
  {
        "state": "backend.schedule.states.main.MainMenu",
        "dcount": 5
    },
```

