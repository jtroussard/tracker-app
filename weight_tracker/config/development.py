import os


class Config(object):
    SERVER_NAME = "localhost:8001"
    DEBUG = True
    BASE_URL = "http://localhost:8001"
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")


class TestingConfig(object):
    BASE_URL = "http://localhost:8001"
