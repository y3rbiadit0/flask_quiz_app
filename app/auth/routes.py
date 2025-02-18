import flask_login
from flask import Blueprint, render_template, request, redirect, url_for

from ..extensions import db, bcrypt
from ..models import Users

auth_blueprint = Blueprint('auth', __name__, url_prefix='/auth')


@auth_blueprint.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        bytes = request.form.get("password")
        # Generate a salt and hash the password

        hashed_password = bcrypt.generate_password_hash(bytes)
        user = Users(username=request.form.get("username"),
                     password=hashed_password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("auth.login"))
    return render_template("sign_up.html")


@auth_blueprint.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        db_user = Users.query.filter_by(
            username=request.form.get("username")).first()
        pwd_form_bytes = request.form.get("password").encode()

        if db_user and bcrypt.check_password_hash(db_user.password, pwd_form_bytes):
            flask_login.login_user(db_user)
            return redirect(url_for("home.home"))
    return render_template("login.html")


@auth_blueprint.route("/logout")
def logout():
    flask_login.logout_user()
    return redirect(url_for("home.home"))
