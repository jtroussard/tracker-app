# Desc: Production configuration file for the Flask application.
from decouple import Config, RepositoryEnv

DOTENV_FILE = "/path/to/.env"
env_config = Config(RepositoryEnv(DOTENV_FILE))


class ProdConfig:
    ENV = "production"
    PORT = env_config("PORT")
    # Load sensitive information from environment variables or .env file
    SQLALCHEMY_DATABASE_URI = env_config("SQLALCHEMY_DATABASE_URI")
    SECRET_KEY = env_config("SECRET_KEY")
    TESTING = env_config("TESTING")
    RATELIMIT_STORAGE_URI = env_config("RATELIMIT_STORAGE_URI")
    RATELIMIT_STORAGE_OPTIONS = env_config("RATELIMIT_STORAGE_OPTIONS")
    RATELIMIT_STRATEGY = env_config("RATELIMIT_STRATEGY")
