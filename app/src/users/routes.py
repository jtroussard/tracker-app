"""
This is a Flask blueprint module that contains routes related to user
functionality.

Routes:
/login: renders a login form and handles user authentication.
/register: renders a registration form and handles adding users.
/logout: logs current user out of current session.
/account: renders user information.
"""
from datetime import datetime
from flask import render_template, redirect, url_for, flash, Blueprint
from flask_login import login_required, login_user, current_user, logout_user
from app.src import db, bcrypt
from app.src.users.forms import LoginForm, RegistrationForm
from app.src.models import Member, Entry

users = Blueprint("users", __name__)


@users.route("/login", methods=["POST", "GET"])
def login():
    """
    If the form is submitted and the email and password are correct, then the
    user is logged in and redirected to the tracker page
    :return: The login.html template is being returned.
    """
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))
    form = LoginForm()
    if form.validate_on_submit():
        user = Member.query.filter_by(email=form.email.data, active_record=True).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash("Login Successful", "success")
            return redirect(url_for("main.home"))
        flash("Login Failed. Please check username/password", "danger")
    return render_template("login.html", active_page="login", form=form)


@users.route("/logout")
def logout():
    """
    Route: logs out current user.
    :return: the redirect function, which is redirecting the user to the home.
    """
    logout_user()
    print("log this: user logged out")
    return redirect(url_for("main.home"))


@users.route("/register", methods=["GET", "POST"])
def register():
    """
    The function takes in a form object, validates the form, hashes the
    password, creates a new user object, adds the new user to the database,
    commits the changes to the database, flashes a message to the user, and
    redirects the user to the login page.

    Bugs: Experienced a bug where after registering, user was automatically
    logged in, instead of being redircted to the login in page. I think what
    might of happened has to do with cache. I was logged in with a user, deleted
    the database file. used a create_all(), then opened an icognito window, then
    registered with the same username/credentials as the user I was previously
    logged in with. Check on this later. For now will add logout() before
    redirect for safety.
    :return: the rendered template for the register page.
    """
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))
    form = RegistrationForm()
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
        return redirect(url_for("users.login"))
    return render_template("register.html", active_page="register", form=form)


@users.route("/account", methods=["GET"])
@login_required
def account():
    """
    Renders the account page template and passes the current user's data to the template.
    If the user is not authenticated, redirects to the login page.

    :return: The account.html template with the current user's data.
    """
    if current_user.is_authenticated:
        entries = Entry.query.filter_by(
            user_id=current_user.id, active_record=True
        ).all()
        return render_template(
            "account.html",
            active_page="account",
            user=current_user,
            now=datetime.now(),
            entries=entries,
        )
    return redirect(url_for("users.login"))
