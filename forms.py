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
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from choices import TIME_OF_DAY_CHOICES, MOOD_CHOICES, STATUS_CHOICES
from validators import validate_weight

import datetime


class RegistrationForm(FlaskForm):
    username = StringField(
        "Username", validators=[DataRequired(), Length(min=2, max=20)]
    )
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField(
        "Confirm Password", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Sign Up")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Login")


class TrackerEntryForm(FlaskForm):
    date = DateField("Date", validators=[DataRequired()], default=datetime.date.today)
    time_of_day = SelectField(
        "Time of Day", choices=TIME_OF_DAY_CHOICES, validators=[DataRequired()]
    )
    mood = SelectField("Mood", choices=MOOD_CHOICES)
    status = SelectField("Status", choices=STATUS_CHOICES)
    weight = FloatField("Weight", validators=[validate_weight, DataRequired()])
    measurement_waist = FloatField("Waist")
    keto = IntegerField("Ketosis Level")
    submit = SubmitField("Save")
