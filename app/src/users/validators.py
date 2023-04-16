"""
This module contains custom wtforms field validators for the users blueprint.

Functions:
validate_username(username): checks whether the given username is already in use
    by an active user in the database. Raises a ValidationError if the username
    is not unique.
validate_email(email): checks whether the given email is already in use by an
    active user in the database. Raises a ValidationError if the email is not
    unique.
"""
from wtforms.validators import ValidationError
from weight_tracker.src.models import User


def validate_username(form, username):
    """Validator. Checks whether the database contains an active username.
    Raises:
        ValidationError: Non unique input
    """
    user = User.query.filter_by(username=username.data, active_record=True).first()
    if user:
        raise ValidationError("That username is already in use. Please choose another.")


def validate_email(form, email):
    """Validator. Checkes whether the database contains an active email address.
    Raises:
    ValidationError: Non unique input
    """
    user = User.query.filter_by(email=email.data, active_record=True).first()
    if user:
        raise ValidationError("That email is already in use. Please choose another.")