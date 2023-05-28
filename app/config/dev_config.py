class DevConfig:
    ENV = "development"
    DEBUG = True
    PORT = 12031
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "postgresql://coco:password@localhost:5432/tracker_db_dev"
    SECRET_KEY = "dslfjadsfkjldsa"
    REDIS_HOST = "localhost"
    REDIS_PORT = 6379
    REDIS_DB = 0
    RATELIMIT_STORAGE_URI = "redis://localhost:6379"
    RATELIMIT_STORAGE_OPTIONS = {"socket_connect_timeout": 30}
    RATELIMIT_STRATEGY = "fixed-window"


# log in command:
# psql -U coco -d tracker_db_dev -h localhost -p 5432
# connection string:
# postgresql://coco:password@localhost:5432/my_database
