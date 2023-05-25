"""A function for printing the attributes of an object.

Args:
    obj: The object whose attributes to print.

"""


def print_object_attributes(obj):
    """Prints the attributes of an object.

    Args:
        obj: The object whose attributes to print.
    """
    attributes = dir(obj)
    for attribute in attributes:
        value = getattr(obj, attribute)
        print(f"{attribute}: {value}")


def print_flask_config(app):
    """Prints all the configuration values of a Flask app."""
    with app.app_context():
        for key in app.config:
            print(f"{key}: {app.config[key]}")
