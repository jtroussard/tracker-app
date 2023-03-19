# pylint: disable=wrong-import-position, missing-module-docstring, no-member

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

from weight_tracker.config.development import Config
from weight_tracker.src.filters import get_username_filter

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()  # Handles sessions

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    app.jinja_env.filters["get_username_filter"] = get_username_filter

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from weight_tracker.src.users.routes import users
    from weight_tracker.src.entries.routes import entries
    from weight_tracker.src.main.routes import main

    app.register_blueprint(users)
    app.register_blueprint(entries)
    app.register_blueprint(main)
    return app
