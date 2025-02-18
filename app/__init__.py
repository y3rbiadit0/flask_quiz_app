from flask import Flask

from config import Config
from .auth import auth_blueprint
from .extensions import db, login_manager, bcrypt
from .home.routes import home_blueprint
from .models import Users


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    db.init_app(app)

    with app.app_context():
        db.create_all()

    login_manager.init_app(app)

    @login_manager.user_loader
    def loader_user(user_id):
        return Users.query.get(user_id)

    bcrypt.init_app(app)

    # Register blueprints here
    app.register_blueprint(home_blueprint)
    app.register_blueprint(auth_blueprint)

    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app
