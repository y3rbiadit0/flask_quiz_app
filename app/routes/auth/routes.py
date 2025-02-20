import flask_login
import sqlalchemy.exc
from flask import Blueprint, render_template, request, redirect, url_for, flash

from ...extensions import db, bcrypt
from ...models import User

auth_blueprint = Blueprint("auth", __name__, url_prefix="/auth")


@auth_blueprint.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        try:
            bytes = request.form.get("password")
            confirm_bytes = request.form.get("confirm_password")
            hashed_password = bcrypt.generate_password_hash(bytes)
            if confirm_bytes == bytes:
                user = User(username=request.form.get("username"),
                            password_hash=hashed_password)
                db.session.add(user)
                db.session.commit()
                return redirect(url_for("auth.login"))
            else:
                flash("Passwords don't match")
                return redirect(url_for("auth.register"))
        except sqlalchemy.exc.IntegrityError as e:
            flash("Username not available, choose other username", "danger")
        except Exception as e:
            flash(e, "danger")
    return render_template("sign_up.html")


@auth_blueprint.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        try:
            db_user = User.query.filter_by(
                username=request.form.get("username")).first()
            pwd_form_bytes = request.form.get("password").encode()

            if db_user and bcrypt.check_password_hash(
                    db_user.password_hash, pwd_form_bytes
            ):
                flask_login.login_user(db_user)
                return redirect(url_for("home.home"))
            else:
                flash("Invalid Username or password!", "danger")
        except Exception as e:
            flash(e, "danger")
    return render_template("login.html")


@auth_blueprint.route("/logout")
def logout():
    flask_login.logout_user()
    return redirect(url_for("home.home"))
