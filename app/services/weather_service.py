from datetime import datetime
from typing import Dict, List

import requests
from flask import current_app


def get_weather(city: str = "Fisciano") -> List[Dict]:
    url = (
        f"http://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&cnt=3"
        f"&appid={current_app.config.get('OPEN_WEATHER_API_KEY')}"
    )
    response = requests.get(url)
    data = response.json()
    weather = []
    for forecast_day in data["list"]:
        date_obj = datetime.strptime(forecast_day["dt_txt"], "%Y-%m-%d %H:%M:%S")
        date_str = date_obj.strftime("%A %d %B - %H:%M")

        day_temp = int(forecast_day["main"]["temp_max"])
        night_temp = int(forecast_day["main"]["temp_min"])
        weather.append(
            {
                "date": date_str,
                "day_temp": day_temp,
                "night_temp": night_temp,
            }
        )
    return weather
