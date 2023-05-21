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

def setup_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Create a rotating file handler to log messages to a file
    file_handler = RotatingFileHandler('tracker-app-logger.log', maxBytes=1024 * 1024 * 10, backupCount=5)
    file_handler.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s] %(module)s - %(message)s'))
    logger.addHandler(file_handler)

    # Create a stream handler to log messages to the console
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(logging.Formatter('[%(levelname)s] %(message)s'))
    logger.addHandler(stream_handler)

    return logger

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
    logger = setup_logger()
    app.config.from_object(config_class)
    logger.info(f"Loaded config class: {config_class}")
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

    # Log a message
    logger.info("Flask application initialized.")

    return app
