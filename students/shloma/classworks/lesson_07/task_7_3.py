# 2021-12-14
# shlom41k
# classwork

import json
import datetime
import requests

api_url = 'https://api.openweathermap.org/data/2.5/forecast'

city = "Minsk"

params = {
            'q': city,
            'appid': 'fe6c9ac08e96ecdd33f559f07bc59da7',
            'units': 'metric',
            'cnt': '50'
        }


res = requests.get(api_url, params=params)
data = res.json()

for i in data['list']:
    d_date = datetime.datetime.fromtimestamp(int(i['dt']))
    t = i['main']['temp']
    v = i['wind']['speed']

    print(f"{d_date}, {city}: t = {t} \N{DEGREE SIGN}C, "
          f"wind speed = {v} m/s, weather - {i['weather'][0]['description']}")
