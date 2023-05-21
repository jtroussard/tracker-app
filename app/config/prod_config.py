# Desc: Production configuration file for the Flask application.
from decouple import Config, RepositoryEnv
from app import logger

DOTENV_FILE = '/path/to/.env'
logger.info(f"Loading environment variables from {DOTENV_FILE}")
env_config = Config(RepositoryEnv(DOTENV_FILE))

class ProdConfig:
    ENV = "production"
    PORT = env_config("PORT")
    # Load sensitive information from environment variables or .env file
    SQLALCHEMY_DATABASE_URI = env_config("SQLALCHEMY_DATABASE_URI")
    SECRET_KEY = env_config("SECRET_KEY")
    TESTING = env_config("TESTING")
