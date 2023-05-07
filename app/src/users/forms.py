"""
Forms package for users blueprint.
"""
from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    BooleanField,
    SubmitField,
    DateField,
)
from wtforms.validators import InputRequired, Email, EqualTo, Length
from app.src.users.validators import validate_username, validate_email


class RegistrationForm(FlaskForm):
    """Users registration form."""

    username = StringField(
        "Username",
        validators=[InputRequired(), Length(min=2, max=20), validate_username],
    )
    first_name = StringField(
        "First Name", validators=[InputRequired(), Length(min=2, max=50)]
    )
    middle_name = StringField(
        "Middle Name", validators=[Optional(strip_whitespace=True), Length(min=1, max=50)]
    )
    last_name = StringField(
        "Last Name", validators=[InputRequired(), Length(min=2, max=50)]
    )
    date_of_birth = DateField("Date of Birth", validators=[InputRequired()])
    email = StringField("Email", validators=[InputRequired(), Email(), validate_email])
    location = StringField("Location or Hometown", validators=[Length(min=1, max=50)])
    password = PasswordField("Password", validators=[InputRequired()])
    confirm_password = PasswordField(
        "Confirm Password", validators=[InputRequired(), EqualTo("password")]
    )
    submit = SubmitField("Sign Up")


class LoginForm(FlaskForm):
    """Login form"""

    email = StringField("Email", validators=[InputRequired(), Email()])
    password = PasswordField("Password", validators=[InputRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Login")
