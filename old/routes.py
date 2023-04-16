import sys
from datetime import date

from flask import render_template, redirect, request, url_for, flash, abort
from flask_login import login_required, login_user, current_user, logout_user
from app import app, db, bcrypt
from app.forms import LoginForm, RegistrationForm, EntryForm
from app.utils.helpers import clear_form
from app.models import User, TrackerEntry


@app.route("/clear_form/<form_name>", methods=["POST"])
def clear_form_route(form_name):
    """
    It gets the form class from the current module using the form_name
    parameter, instantiates the form, clears the form, flashes a message, and
    redirects to the register page. Security considerations using sys module

    Security: If the value of form_name is controlled by user input, you need to
    make sure that it can't be manipulated to import arbitrary modules of
    attributes from your system. This could potentially be used to execute
    arbitrary code on your server or access sensitive data. One way to guard
    against this is to use a whitelist of allowed form names and check that the
    requested form is in the whitelist before importing it.

    Namespace collisions: If you have multiple modules that define form classes
    with the same name, using getattr with sys.modules[__name__] could result in
    unintended behavior. In this case, it's better to explicitly import the
    module that defines the form you want to use.

    Readability: Using getattr with sys.modules[__name__] can make your code
    less readable and harder to follow, especially for developers who are not
    familiar with your codebase. It's often better to use explicit imports and
    avoid dynamically importing modules unless it's absolutely necessary.

    :param form_name: The name of the form class to clear
    :return: a redirect to the register page.
    """
    print("clicking clear button")
    form_class = getattr(sys.modules[__name__], form_name)
    form = form_class()
    clear_form(form)
    flash("Form cleared", "info")
    return redirect(url_for("register"))
