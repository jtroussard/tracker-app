# from flask import flash

def clear_form(form):
    """
    Clears all fields in the given form.
    """
    # form.process(data=None)
    print('clearing fields')

# IMPLEMENT THIS LATER
# def flash_errors(form):
#     """
#     Flashes all errors in the given form.
#     """
#     for field, errors in form.errors.items():
#         for error in errors:
#             flash(f"Error in the {getattr(form, field).label.text} field: {error}", "error")
