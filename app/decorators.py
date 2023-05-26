from functools import wraps
from flask import request, abort
from flask_login import current_user

def restrict_access(func):
    """
    Decorator to restrict access to a view function based on user authentication.
    Only authenticated users with specific permissions are allowed to access the 
    decorated route.

    Args:
        func (callable): The view function to be decorated.
    Returns:
        callable: The decorated function.
    Raises:
        HTTPException: 403 Forbidden error if the user is not authenticated or
        lacks the required permissions.
    """
    @wraps(func)
    def decorated_function(*args, **kwargs):
        allowed_users = 'admin'
        if current_user.is_authenticated in allowed_users:
            return func(*args, **kwargs)
        else:
            abort(403) 
    return decorated_function