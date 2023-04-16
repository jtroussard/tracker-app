from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

class Config:
    """
    Base configuration class.
    """
    DEBUG = os.getenv('DEBUG')
    TESTING = os.getenv('TESTING')
    CSRF_ENABLED = os.getenv('CSRF_ENABLED')
    SECRET_KEY = os.getenv('SECRET_KEY_TRACKER_APP')
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")

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



#     import os


# class Config(object):
#     SERVER_NAME = "localhost:8001"
#     DEBUG = True
#     BASE_URL = "http://localhost:8001"
#     SECRET_KEY = os.environ.get("SECRET_KEY")
#     SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")


# class TestingConfig(object):
#     BASE_URL = "http://localhost:8001"
