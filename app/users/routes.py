# pylint: disable=wrong-import-position, missing-module-docstring, line-too-long

"""
This module contains the routes for handling user authentication and management.

The following routes are defined in this module:

/login: Handles the login process for the application.
/logout: Logs the user out of the application.
/register: Registers a new user for the application.
/account: Renders the account page for the logged-in user.

The routes in this module require the user to be authenticated, except for the
/login route. If the user is not authenticated, the routes will redirect the
user to the login page.
"""
from datetime import datetime
import logging

LOG = logging.getLogger(__name__)

from sqlalchemy import desc

from flask import render_template, redirect, url_for, flash, Blueprint
from flask_login import login_required, login_user, current_user, logout_user
from app import db, bcrypt
from app.users.forms import LoginForm, RegistrationForm
from app.models import Member, Entry

users = Blueprint("users", __name__)


@users.route("/login", methods=["POST", "GET"])
def login():
    """
    This function handles the login process for the application.

    Returns:
    * A redirect to the home page if the login is successful.
    * A render of the login template if the login is unsuccessful.
    """

    # Check if the user is already authenticated.
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))

    # Create a new form object.
    form = LoginForm()

    # If the form is submitted and valid, try to log the user in.
    # pylint: disable=no-else-return
    if form.validate_on_submit():
        user = Member.query.filter_by(email=form.email.data, active_record=True).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash("Login Successful", "success")
            return redirect(url_for("main.home"))
        else:
            flash("Login Failed. Please check username/password", "danger")
    return render_template("login.html", active_page="login", form=form)


@users.route("/logout")
def logout():
    """
    This function logs the user out of the application.

    Returns:
    * A redirect to the home page.
    """

    # Log the user out.
    logout_user()

    # Print a log message.
    # print("log this: user logged out")

    # Redirect the user to the home page.
    return redirect(url_for("main.home"))


@users.route("/register", methods=["GET", "POST"])
def register():
    """
    This function registers a new user for the application.

    Returns:
    * A render of the register template if the registration is unsuccessful.
    * A redirect to the login page if the registration is successful.
    """

    # Check if the user is already authenticated.
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))

    # Create a new form object.
    form = RegistrationForm()

    # If the form is submitted and valid, create a new user and redirect the user to the login page.
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode("utf8")
        new_user = Member(
            username=form.username.data,
            first_name=form.first_name.data,
            middle_name=form.middle_name.data,
            last_name=form.last_name.data,
            date_of_birth=form.date_of_birth.data,
            email=form.email.data,
            password=hashed_pw,
            joined_date=datetime.now(),
        )
        db.session.add(new_user)
        db.session.commit()
        logout_user()
        flash("Your account has been created. You may now login.", "success")
        LOG.info(
            "New user registered: %s, %s", form.username.data, Member.query.count()
        )
        return redirect(url_for("users.login"))

    # Otherwise, render the register template.
    return render_template("register.html", active_page="register", form=form)


@users.route("/account", methods=["GET"])
@login_required
def account():
    """
    This function renders the account page for the logged-in user.

    Returns:
    * A render of the account template.
    """

    # Check if the user is authenticated.
    if not current_user.is_authenticated:
        return redirect(url_for("users.login"))

    # Get the user's entries.
    entries = (
        Entry.query.filter_by(user_id=current_user.id, active_record=True)
        .order_by(desc(Entry.date))
        .all()
    )

    # Render the account template.
    return render_template(
        "account.html",
        active_page="account",
        user=current_user,
        now=datetime.now(),
        entries=entries,
    )
