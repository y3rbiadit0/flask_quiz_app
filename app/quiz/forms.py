from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField
from wtforms.validators import DataRequired


class QuizForm(FlaskForm):
    answer = RadioField("Choose an answer", coerce=int, validators=[DataRequired()])
    submit = SubmitField("Submit")
