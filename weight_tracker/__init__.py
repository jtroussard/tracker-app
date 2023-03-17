# pylint: disable=wrong-import-position, missing-module-docstring

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

from weight_tracker.config.development import Config
from weight_tracker.filters import get_username_filter

app = Flask(__name__)
app.config.from_object(Config)
app.config["SECRET_KEY"] = "this-is-a-super-secret-key-wubalubadubdub"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

app.jinja_env.filters['get_username_filter'] = get_username_filter

db = SQLAlchemy()
db.init_app(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app) # Handles sessions

from weight_tracker import routes
