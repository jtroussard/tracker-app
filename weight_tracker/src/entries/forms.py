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
from wtforms.validators import InputRequired
from weight_tracker.src.constants.choices import (
    TIME_OF_DAY_CHOICES,
    MOOD_CHOICES,
    STATUS_CHOICES,
)
from weight_tracker.src.entries.validators import validate_weight


class EntryForm(FlaskForm):
    """Entry form of FlaskForm"""

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
