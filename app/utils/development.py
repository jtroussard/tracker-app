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
