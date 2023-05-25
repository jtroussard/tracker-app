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
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_redis import FlaskRedis

# from app.utils.development import print_object_attributes, print_flask_config

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
migrate = Migrate()
limiter = Limiter(key_func=get_remote_address)
redis_client = FlaskRedis()


def configure_logging(app):
    # Create a formatter
    formatter = "[%(asctime)s] [%(levelname)s] [%(message)s]"

    # Register root logging
    logging.basicConfig(
        level=logging.DEBUG,
        format=formatter,
        handlers=[
            RotatingFileHandler("./logs/flask.log", maxBytes=1048576, backupCount=5)
        ],
    )

    # Add a StreamHandler for development mode
    if app.debug:
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.DEBUG)
        stream_handler.setFormatter(formatter)
        logging.getLogger().addHandler(stream_handler)

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
    configure_logging(app)
    app.config.from_object(config_class)
    app.logger.info(f"Creating app with config: {config_class.__name__}")
    register_filters(app)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "users.login"
    migrate.init_app(app, db)
    limiter.init_app(app)
    redis_client.init_app(app)

    # Register blueprints
    from app.main.routes import main
    from app.users.routes import users
    from app.entries.routes import entries
    from app.api.routes import api

    app.register_blueprint(users)
    app.register_blueprint(entries)
    app.register_blueprint(main)
    app.register_blueprint(api)

    return app
