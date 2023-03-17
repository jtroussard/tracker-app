from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from weight_tracker.config.development import Config

db = SQLAlchemy()

app = Flask(__name__)
app.config.from_object(Config)
app.config["SECRET_KEY"] = "this-is-a-super-secret-key-wubalubadubdub"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

db.init_app(app)

from weight_tracker import routes