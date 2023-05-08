"""
Forms package for entries blueprint.
"""
import datetime
from flask_wtf import FlaskForm
from wtforms import (
    SubmitField,
    DateField,
    SelectField,
    FloatField,
    IntegerField,
)
from wtforms.validators import InputRequired, Optional
from app.src.constants.choices import (
    TIME_OF_DAY_CHOICES,
    MOOD_CHOICES,
    STATUS_CHOICES,
)
from app.src.entries.validators import validate_weight, validate_min_max_float


class EntryForm(FlaskForm):
    """Entry form of FlaskForm"""

    date = DateField("Date", validators=[InputRequired()], default=datetime.date.today)
    time_of_day = SelectField(
        "Time of Day", choices=TIME_OF_DAY_CHOICES, validators=[InputRequired()]
    )
    mood = SelectField("Mood", choices=MOOD_CHOICES)
    status = SelectField("Status", choices=STATUS_CHOICES)
    weight = FloatField("Weight", validators=[InputRequired(), validate_weight])
    measurement_waist = FloatField(
        "Waist", validators=[Optional(strip_whitespace=True), validate_min_max_float]
    )
    keto = IntegerField("Ketosis Level", validators=[Optional(strip_whitespace=True), validate_min_max_float])
    submit = SubmitField("Save")
