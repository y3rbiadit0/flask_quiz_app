from flask import Blueprint, render_template, request

from ...services import get_weather

home_blueprint = Blueprint("home", __name__)



@home_blueprint.route('/', methods=['GET', 'POST'])
def home():
    default_city = "Fisciano"
    if request.method == 'POST':
        city = request.form['city']
        weather_data = get_weather(city)
    else:
        weather_data = get_weather(default_city)
    return render_template("home.html", weather_data=weather_data)
