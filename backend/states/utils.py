import requests


def get_today_schedule():
    response = requests.get('https://mathschool.mai.ru/api/org/schedule/today')
    json = response.json()
    return json

def get_next_day_schedule():
    response = requests.get('https://mathschool.mai.ru/api/org/schedule/nextday')
    json = response.json()
    return json
