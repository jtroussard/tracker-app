import os, json

import json

try:
    with open("/etc/tracker_app-config.json") as config_file:
        config = json.load(config_file)
except FileNotFoundError:
    with open(os.path.join(os.path.dirname(__file__), "default.json")) as config_file:
        config = json.load(config_file)


class Config:
    """
    Base configuration class.
    """

    DEBUG = os.getenv("DEBUG")
    TESTING = config.get("TESTING")
    CSRF_ENABLED = config.get("CSRF_ENABLED")
    SECRET_KEY = config.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = config.get("SQLALCHEMY_DATABASE_URI")
    PORT = config.get("PORT")


class ProductionConfig(Config):
    """
    Production configuration class.
    """

    DEBUG = False
    PORT = 8001


class DevelopmentConfig(Config):
    """
    Development configuration class.
    """

    DEVELOPMENT = True
    DEBUG = True
    PORT = 8001


class TestingConfig(Config):
    """
    Testing configuration class.
    """

    TESTING = True
    PORT = 8001
