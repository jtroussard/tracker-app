# pylint: disable=too-few-public-methods
"""Models module for flask application weight tracker"""
from datetime import datetime

from flask_login import UserMixin  # For common attributes/methods for User

from app import db, login_manager


@login_manager.user_loader
def load_user(user_id):
    """Tells extension how to get a user."""
    return Member.query.get(int(user_id))


class Member(db.Model, UserMixin):

    """A class representing a member of the website.

    Attributes:
        id: The member's ID.
        username: The member's username.
        first_name: The member's first name.
        middle_name: The member's middle name.
        last_name: The member's last name.
        date_of_birth: The member's date of birth.
        location: The member's location.
        email: The member's email address.
        image_file: The member's profile image file name.
        password: The member's password.
        joined_date: The date the member joined the website.
        active_record: Whether the member's account is active.
        entry: A relationship to the member's entries.

    Methods:
        __repr__(): Returns a string representation of the member.
    """

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
        """Returns a string representation of the member."""
        return f"Member({self.username})"


class Entry(db.Model):

    """A class representing an entry in the website.

    Attributes:
        id: The entry's ID.
        date: The date the entry was created.
        time_of_day: The time of day the entry was created.
        mood: The entry's mood.
        status: The entry's status.
        weight: The entry's weight.
        measurement_waist: The entry's waist measurement.
        keto: The entry's keto status.
        user_id: The ID of the member who created the entry.
        active_record: Whether the entry is active.

    Methods:
        __repr__(): Returns a string representation of the entry.
        __eq__(): Returns True if the entry is equal to another entry, False otherwise.
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
    user_id = db.Column(db.Integer, db.ForeignKey("member.id"), nullable=False)
    active_record = db.Column(db.Boolean(), nullable=False, default=True)
    weight_difference = db.Column(db.Integer, nullable=False, default=0)

    def calculate_weight_difference(self):
        # Get the previous entry based on the date
        previous_entry = (
            Entry.query.filter(
                Entry.date < self.date,
                Entry.user_id == self.user_id,
                Entry.active_record.is_(True),
            )
            .order_by(Entry.date.desc())
            .first()
        )

        if previous_entry:
            if self.weight > previous_entry.weight:
                self.weight_difference = 1  # Gain
            elif self.weight < previous_entry.weight:
                self.weight_difference = -1  # Loss
            else:
                self.weight_difference = 0  # No change
        else:
            self.weight_difference = 0  # No change for the first entry

    def save(self):
        # Calculate the weight difference before saving
        self.calculate_weight_difference()
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        """Returns a string representation of the entry."""
        return (
            f"Entry('{self.id}: Author={self.user_id}, "
            f"Weight={self.weight}, Active='{self.active_record}')"
        )

    def __eq__(self, other):
        """Returns True if the entry is equal to another entry, False otherwise."""
        if isinstance(other, Entry):
            return (
                self.id == other.id
                and self.date == other.date
                and self.weight == other.weight
                and self.time_of_day == other.time_of_day
                and self.mood == other.mood
                and self.status == other.status
                and self.measurement_waist == other.measurement_waist
                and self.keto == other.keto
                and self.active_record == other.active_record
            )
        return False
