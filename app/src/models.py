# pylint: disable=too-few-public-methods
"""Models module for flask application weight tracker"""
from datetime import datetime

from flask_login import UserMixin  # For common attributes/methods for User

from app.src import db, login_manager


@login_manager.user_loader
def load_user(user_id):
    """Tells extension how to get a user."""
    return Member.query.get(int(user_id))


class Member(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    first_name = db.Column(db.String(50), unique=False, nullable=False)
    middle_name = db.Column(db.String(50), unique=False, nullable=True)
    last_name = db.Column(db.String(50), unique=False, nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)  # age validation needed
    location = db.Column(db.String(50))
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default="default.jpg")
    password = db.Column(db.String(60), nullable=False)
    joined_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    active_record = db.Column(db.Boolean(), nullable=False, default=True)
    entry = db.relationship("Entry", backref="author", lazy="select")

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow
    )  # pass the function not the return value
    time_of_day = db.Column(db.String(20))
    mood = db.Column(db.String(20))
    status = db.Column(db.String(20))
    weight = db.Column(db.Float(), nullable=False)
    measurement_waist = db.Column(db.Float())
    keto = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey("member.id"), nullable=False)
    active_record = db.Column(db.Boolean(), nullable=False, default=True)

    def __repr__(self):
        return f"Entry('{self.date}', '{self.weight}')"
