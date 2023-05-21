# pylint: disable=wrong-import-position, missing-module-docstring, no-member, import-outside-toplevel

"""
A module for creating a Flask application.

This module provides functions for creating a Flask application, registering
filters, and registering blueprints.

Functions:
    create_app(config_class): Creates a Flask application.
    register_filters(app): Registers filters with the Flask application.
"""
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate

from app.utils.development import print_object_attributes

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
migrate = Migrate()


def configure_logging():
    # Create a formatter
    formatter = "[%(asctime)s] [%(levelname)s] [%(message)s]"

    # register root logging
    logging.basicConfig(
        level=logging.DEBUG,
        format=formatter,
        handlers=[
            RotatingFileHandler("./logs/flask.log", maxBytes=1048576, backupCount=5)
        ],
    )
    logging.getLogger("werkzeug").setLevel(logging.INFO)


def register_filters(app):
    """Registers filters with the Flask application.
    Args:
        app: The Flask application.
    """
    from app.filters import (
        get_username_filter,
        get_month_name,
        get_user_fullname,
        get_pretty_date,
    )

    app.jinja_env.filters["get_username_filter"] = get_username_filter
    app.jinja_env.filters["get_month_name"] = get_month_name
    app.jinja_env.filters["get_user_fullname"] = get_user_fullname
    app.jinja_env.filters["get_pretty_date"] = get_pretty_date


def create_app(config_class):
    """Creates a Flask application.
    Args:
        config_class: The class that defines the Flask application's configuration.

    Returns:
        The Flask application.
    """
    app = Flask(__name__)
    configure_logging()
    app.config.from_object(config_class)
    app.logger.info(f"Creating app with config: {config_class.__name__}")
    register_filters(app)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "users.login"
    migrate.init_app(app, db)

    # Register blueprints
    from app.main.routes import main
    from app.users.routes import users
    from app.entries.routes import entries

    app.register_blueprint(users)
    app.register_blueprint(entries)
    app.register_blueprint(main)

    return app
