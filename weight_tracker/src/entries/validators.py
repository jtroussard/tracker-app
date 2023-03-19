"""
This module contains custom wtforms field validators for the entries blueprint.

Functions:
validate_weight(field): checks whether weight field input is three digit number
    with a maximum of one decimal place value.
"""
from wtforms.validators import ValidationError


def validate_weight(form, field):
    """Checks whether weight field input is three digit number with a maximum of
     one decimal place value.

    Args:
        field (FloatField): _description_

    Raises:
        ValidationError: Input data type check
        ValidationError: Numerical format and range check
    """
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
