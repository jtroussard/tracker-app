from wtforms.validators import ValidationError
from weight_tracker.models import User


def validate_weight2(form, field):
    if field.data is not None:
        whole_number = int(field.data)
        decimal_places = (
            len(str(field.data).split(".")[1]) if "." in str(field.data) else 0
        )
        if whole_number > 999 or decimal_places > 1:
            raise ValidationError(
                "Weight must be less than or equal to 999 and have only one decimal place"
            )

def validate_username(form, username):
    user = User.query.filter_by(username=username.data).first()
    if user:
        raise ValidationError('That username is already in use. Please choose another.')

def validate_email(form, email):
    user = User.query.filter_by(email=email.data).first()
    if user:
        raise ValidationError('That email is already in use. Please choose another.')

def validate_weight(form, field):
    if field.data is not None:
        whole_number = None
        decimal_places = None
        if isinstance(field.data, (int, float)):
            whole_number = int(field.data)
            decimal_places = (
                len(str(field.data).split(".")[1]) if "." in str(field.data) else 0
            )
        else:
            raise ValidationError("Weight must be a number")

        if whole_number > 999 or decimal_places > 1:
            raise ValidationError(
                "Weight must be less than or equal to 999 and have only one decimal place"
            )
