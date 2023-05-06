# pylint: disable=wrong-import-position, missing-module-docstring, no-member

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate


from app.config import ProductionConfig, Config
from app.src.filters import get_username_filter, get_month_name, get_user_fullname

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()  # Handles sessions
migrate = Migrate()

# Don't forget to set the env when going prod, including the base config variables.
def create_app(config_class=Config):
    app.jinja_env.filters["get_username_filter"] = get_username_filter
    app.jinja_env.filters["get_month_name"] = get_month_name
    app.jinja_env.filters["get_user_fullname"] = get_user_fullname

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    from app.src.users.routes import users
    from app.src.entries.routes import entries
    from app.src.main.routes import main

    app.register_blueprint(users)
    app.register_blueprint(entries)
    app.register_blueprint(main)
    return app
