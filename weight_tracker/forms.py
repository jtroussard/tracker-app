from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    SubmitField,
    BooleanField,
    DateField,
    SelectField,
    FloatField,
    IntegerField,
)
from wtforms.validators import InputRequired, Length, Email, EqualTo
from weight_tracker.constants.choices import TIME_OF_DAY_CHOICES, MOOD_CHOICES, STATUS_CHOICES
from weight_tracker.utils.validators import validate_weight, validate_username, validate_email

import datetime

class RegistrationForm(FlaskForm):
    username = StringField(
        "Username", validators=[InputRequired(), Length(min=2, max=20), validate_username]
    )
    email = StringField("Email", validators=[InputRequired(), Email(), validate_email])
    password = PasswordField("Password", validators=[InputRequired()])
    confirm_password = PasswordField(
        "Confirm Password", validators=[InputRequired(), EqualTo("password")]
    )
    submit = SubmitField("Sign Up")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[InputRequired(), Email()])
    password = PasswordField("Password", validators=[InputRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Login")


class TrackerEntryForm(FlaskForm):
    date = DateField("Date", validators=[InputRequired()], default=datetime.date.today)
    time_of_day = SelectField(
        "Time of Day", choices=TIME_OF_DAY_CHOICES, validators=[InputRequired()]
    )
    mood = SelectField("Mood", choices=MOOD_CHOICES)
    status = SelectField("Status", choices=STATUS_CHOICES)
    weight = FloatField("Weight", validators=[validate_weight, InputRequired()])
    measurement_waist = FloatField("Waist")
    keto = IntegerField("Ketosis Level")
    submit = SubmitField("Save")
