"""Filters for flask application weight-tracker"""


def get_username_filter(current_user):
    """
    If the user is logged in, return their username, otherwise return an empty
    string

    :param current_user: The current user object from flask_login
    :return: A string.
    """
    print(current_user)
    if current_user.is_authenticated:
        return current_user.username
    return ""
