from flask import Blueprint, render_template

from ...services import get_cached_weather

home_blueprint = Blueprint("home", __name__)


@home_blueprint.route("/")
def home():
    city = "Fisciano"
    weather_data = get_cached_weather(city)
    return render_template("home.html", weather_data=weather_data)
