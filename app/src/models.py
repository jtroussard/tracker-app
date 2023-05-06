# pylint: disable=too-few-public-methods
"""Models module for flask application weight tracker"""
from datetime import datetime

from flask_login import UserMixin  # For common attributes/methods for User

from app.src import db, login_manager

# Going to need to do some secret stuff in here use from flask import current_app


@login_manager.user_loader
def load_user(user_id):
    """Tells extension how to get a user."""
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    """A class representing a user.

    Args:
        id (int): The user's ID.
        username (str): The user's username, unique and non-null.
        email (str): The user's email address, unique and non-null.
        image_file (str): The name of the user's profile image file, non-null
            with a default value of 'default.jpg'.
        password (str): The user's password, non-null.
        entry (list): A list of the user's tracker entries.

    Attributes:
        id (int): The user's ID.
        username (str): The user's username, unique and non-null.
        email (str): The user's email address, unique and non-null.
        image_file (str): The name of the user's profile image file, non-null
            with a default value of 'default.jpg'.
        password (str): The user's password, non-null.
        entry (list): A list of the user's tracker entries.

    Methods:
        __repr__(self): Returns a string representation of the User object.

    """

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    first_name = db.Column(db.String(50), unique=False, nullable=False)
    middle_name = db.Column(db.String(50), unique=False, nullable=True)
    last_name = db.Column(db.String(50), unique=False, nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False) # age validation needed
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default="default.jpg")
    password = db.Column(db.String(60), nullable=False)
    joined_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    active_record = db.Column(db.Boolean(), nullable=False, default=True)
    entry = db.relationship("Entry", backref="author", lazy="select")

    def __repr__(self):
        """
        :return: The username, email, and image file of the user.
        """
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Entry(db.Model):
    """The Entry class is a model that represents a single entry in the
    tracker. It has a date, time of day, mood, status, weight,
    measurement_waist, keto, and user_id
    """

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
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    active_record = db.Column(db.Boolean(), nullable=False, default=True)

    def __repr__(self):
        """
        :return: The date and weight of the entry.
        """
        return f"Entry('{self.date}', '{self.weight}')"
