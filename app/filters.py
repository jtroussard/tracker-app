"""A module for providing utility functions.

This module provides functions for getting the username filter, the month name,
the user full name, and the pretty date.

Functions:
    get_username_filter(current_user): Returns the username of the current
    user, if they are authenticated.
    get_month_name(month_number): Returns the name of the month corresponding
    to the given month number.
    get_user_fullname(name): Returns the full name of the user, given their
    first and last names.
    get_pretty_date(value): Returns a pretty date string from a datetime object.
"""

import calendar
from datetime import datetime


def get_username_filter(current_user):
    """Returns the username of the current user, if they are authenticated.
    Args:
        current_user: The current user.

    Returns:
        The username of the current user, if they are authenticated.
    """
    if current_user.is_authenticated:
        return current_user.username
    return ""


def get_month_name(month_number):
    """Returns the name of the month corresponding to the given month number.
    Args:
        month_number: The month number.

    Returns:
        The name of the month corresponding to the given month number.
    """
    return calendar.month_name[month_number]


def get_user_fullname(name):
    """Returns the full name of the user, given their first and last names.
    Args:
        name: A dictionary containing the user's first and last names.

    Returns:
        The full name of the user, given their first and last names.
    """
    if not name["middle_name"]:
        return f"{name['first_name']} {name['last_name']}"
    return (
        f"{name['first_name']} " f"{name['middle_name'][0:1]}. " f"{name['last_name']}"
    )


def get_pretty_date(value):
    """Returns a pretty date string from a datetime object.
    Args:
        value: A datetime object.

    Returns:
        A pretty date string from a datetime object.
    """
    ugly_date_str = value.strftime("%Y-%m-%d %H:%M:%S")
    pretty_date = datetime.strptime(ugly_date_str, "%Y-%m-%d %H:%M:%S")
    return pretty_date.strftime("%B %d, %Y")
