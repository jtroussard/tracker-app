# pylint: disable=wrong-import-position, missing-module-docstring

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

from weight_tracker.config.development import Config

app = Flask(__name__)
app.config.from_object(Config)
app.config["SECRET_KEY"] = "this-is-a-super-secret-key-wubalubadubdub"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

db = SQLAlchemy()
db.init_app(app)
bcrypt = Bcrypt(app)

from weight_tracker import routes
