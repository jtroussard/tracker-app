from decouple import config


class ProdConfig:
    ENV = "production"
    PORT = 8888
    # Load sensitive information from environment variables or .env file
    SQLALCHEMY_DATABASE_URI = config("SQLALCHEMY_DATABASE_URI")
    SECRET_KEY = config("SECRET_KEY")
    API_KEY = config("API_KEY")
