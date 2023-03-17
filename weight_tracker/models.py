# pylint: disable=too-few-public-methods

from datetime import datetime
from weight_tracker import db

class User(db.Model):
    """The User class is a model that will be stored in a table called users.
    The table will have columns for id, username, email, image_file, and
    password. The id column will be the primary key, and the username and email
    columns will be unique. The image_file column will have a default value of
    default.jpg. The password column will be hashed using the
    werkzeug.security.generate_password_hash() function
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default="default.jpg")
    password = db.Column(db.String(60), nullable=False)
    entry = db.relationship("TrackerEntry", backref="author", lazy="select")

    def __repr__(self):
        """
        The __repr__ function is used to display the object in a way that is
        unambiguous and can be used to recreate the object
        :return: The username, email, and image file of the user.
        """
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class TrackerEntry(db.Model):
    """The TrackerEntry class is a model that represents a single entry in the
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

    def __repr__(self):
        """
        `__repr__` is a special function that returns a string representation of
        the object
        :return: The date and weight of the entry.
        """
        return f"TrackerEntry('{self.date}', '{self.weight}')"
