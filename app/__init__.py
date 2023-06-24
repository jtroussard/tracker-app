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

def get_config_class(environment):
    """Get the configuration class based on the environment.

    Args:
        environment: The environment name ('development', 'testing', 'production').

    Returns:
        The configuration class.
    """
    if environment == 'development':
        from app.config.dev_config import DevConfig
        return DevConfig
    elif environment == 'testing':
        from app.config.testing_config import TestingConfig
        return TestingConfig
    elif environment == 'production':
        from app.config.prod_config import ProdConfig
        return ProdConfig
    else:
        raise ValueError(f"Invalid environment: {environment}")

def configure_logging(app):
    # Create a formatter
    formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] [%(message)s]")

    # Create a file handler
    file_handler = logging.FileHandler("logs/flask.log")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    # Set the file handler for the root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)
    root_logger.addHandler(file_handler)

    # Set the level for werkzeug logger
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


def create_app(environment):
    """Creates a Flask application.
    Args:
        config_class: The class that defines the Flask application's configuration.

    Returns:
        The Flask application.
    """
    app = Flask(__name__)
    configure_logging(app)
    config_class = get_config_class(environment)
    app.config.from_object(config_class)
    app.logger.info(f"Creating app with config: {config_class.__name__}")
    register_filters(app)

    print("PIZZA")

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "users.login" # type: ignore
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
