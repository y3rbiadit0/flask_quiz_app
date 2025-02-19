from typing import Dict, List

import requests
from flask import current_app

from ..extensions import cache


def _get_weather(city: str = "Fisciano") -> List[Dict]:
    url = (
        f"http://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&cnt=3"
        f"&appid={current_app.config.get('OPEN_WEATHER_API_KEY')}"
    )
    response = requests.get(url)
    data = response.json()
    weather = []
    for forecast_day in data["list"]:  # Three days
        day_temp = forecast_day["main"]["temp_max"]
        night_temp = forecast_day["main"]["temp_min"]
        weather.append(
            {
                "date": forecast_day["dt_txt"],
                "day_temp": day_temp,
                "night_temp": night_temp,
            }
        )
    return weather


# Cache the weather data for 10 minutes (300 seconds)
@cache.cached(timeout=300, key_prefix="weather_data")
def get_cached_weather(city: str = "Fisciano") -> List[Dict]:
    return _get_weather(city)
