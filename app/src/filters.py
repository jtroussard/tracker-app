import calendar

"""Filters for flask application weight-tracker"""

def get_username_filter(current_user):
    """
    If the user is logged in, return their username, otherwise return an empty
    string

    :param current_user: The current user object from flask_login
    :return: A string.
    """
    if current_user.is_authenticated:
        return current_user.username
    return ""


def get_month_name(month_number):
    return calendar.month_name[month_number]

def get_user_fullname(name):
    if not name['middle_name']:
        return f"{name['first_name']} {name['last_name']}"
    return f"{name['first_name']} {name['middle_name'][0:1]}. {name['last_name']}"
