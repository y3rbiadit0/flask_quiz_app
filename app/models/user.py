from flask_login import UserMixin

from ..extensions import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), unique=True, nullable=False)
    password_hash = db.Column(db.String(250), nullable=False)
