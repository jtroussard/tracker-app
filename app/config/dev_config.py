class DevConfig:
    ENV = "development"
    DEBUG = True
    PORT = 12031
    SERVER_NAME = 'localhost:12031'
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "postgresql://lester:green@database_tracker:5432/dockertestdb"
    DB_USERNAME = "lester"
    DB_PASSWORD = "green"
    DB_NAME = "dockertestdb"
    SECRET_KEY = "dslfjadsfkjldsa"
    REDIS_HOST = "localhost"
    REDIS_PORT = 6379
    REDIS_DB = 0
    RATELIMIT_STORAGE_URI = "redis://localhost:6379"
    RATELIMIT_STORAGE_OPTIONS = {"socket_connect_timeout": 30}
    RATELIMIT_STRATEGY = "fixed-window"


# log in command:
# psql -U coco -d my_database -h localhost -p 5432
# connection string:
# postgresql://coco:password@localhost:5432/my_database
