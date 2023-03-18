import sys
from datetime import date

from flask import render_template, redirect, request, url_for, flash, abort
from flask_login import login_required, login_user, current_user, logout_user
from weight_tracker import app, db, bcrypt
from weight_tracker.forms import LoginForm, RegistrationForm, TrackerEntryForm
from weight_tracker.utils.helpers import clear_form
from weight_tracker.models import User, TrackerEntry


@app.route("/")
@app.route("/home")
def home():
    """
    The function home() returns the rendered template "home.html" with the
    variables active_page and
    :return: The home.html file is being returned.
    """
    return render_template("home.html", active_page="home")


@app.route("/tracker/<int:entry_id>", methods=["GET"])
@login_required
def get_entry(entry_id):
    print("get entry start")
    entry = TrackerEntry.query.filter_by(
        id=entry_id, active_record=True
    ).first_or_404()
    if entry.author != current_user:
        abort(403)
    # entry = TrackerEntry.query.get_or_404(entry_id).filter_by(TrackerEntry.active_record == True)
    return render_template("entry.html", entry=entry)


@app.route("/tracker/<int:entry_id>/update", methods=["GET", "PUT", "POST"])
@login_required
def update_entry(entry_id):
    entry = TrackerEntry.query.filter_by(
        id=entry_id, active_record=True
    ).first_or_404()
    if entry.author != current_user:
        abort(403)
    form = TrackerEntryForm(obj=entry)
    if request.method == "POST":
        print("log this: Request method is POST")
        if form.validate_on_submit():
            print("log this: Form validated successfully")
            form.populate_obj(entry)
            db.session.commit()
            flash("Your entry has been updated!", "success")
            return redirect(url_for("get_entry", entry_id=entry_id))
        # else:
        #     print("Form did not validate")
        #     print(f"{form.errors}")
    return render_template("entry_edit.html", form=form, entry=entry)


@app.route("/tracker/<int:entry_id>", methods=["POST"])
@login_required
def delete_entry(entry_id):
    entry = TrackerEntry.query.filter_by(
        id=entry_id, active_record=True
    ).first_or_404()
    if entry.author != current_user:
        abort(403)
    else:
        entry.active_record = False
        db.session.commit()
        flash("Your entry has been deleted!", "success")
    return redirect(url_for("tracker_index"))


@app.route("/tracker_index", methods=["GET", "POST"])
@login_required
def tracker_index():
    """
    The function get_tracker() is called when the user visits the /tracker route.
    :return: The tracker page is being returned.
    """
    if current_user.is_authenticated:
        entries = TrackerEntry.query.filter_by(
            user_id=current_user.id, active_record=True
        ).all()
        form = TrackerEntryForm()
        if form.validate_on_submit():
            entry = TrackerEntry(
                date=form.date.data,
                time_of_day=form.time_of_day.data,
                mood=form.mood.data,
                status=form.status.data,
                weight=form.weight.data,
                measurement_waist=form.measurement_waist.data,
                keto=form.keto.data,
                user_id=current_user.id,
            )
            db.session.add(entry)
            db.session.commit()
            flash(f"You have submitted entry: {entry}", "success")
            return redirect(url_for("tracker_index"))
        return render_template(
            "tracker.html",
            active_page="tracker",
            entries=entries,
            form=form,
        )
    return redirect(url_for("home"))


@app.route("/login", methods=["POST", "GET"])
def login():
    """
    If the form is submitted and the email and password are correct, then the
    user is logged in and redirected to the tracker page
    :return: The login.html template is being returned.
    """
    if current_user.is_authenticated:
        print(vars(current_user))
        return redirect(url_for("home"))
    # for now we will redefine  here - TODO check login status and set variable as needed
    name = ""
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(
            email=form.email.data, active_record=True
        ).first()
        if user and bcrypt.check_password_hash(
            user.password, form.password.data
        ):
            login_user(user, remember=form.remember.data)
            flash("Login Successful", "success")
            return redirect(url_for("home"))
        else:
            flash(
                "Login Unsuccessful. Please check username and password",
                "danger",
            )
    return render_template("login.html", active_page="login", form=form)


@app.route("/logout")
def logout():
    """
    The function logout() is called when the user clicks the logout button. The function logout_user()
    is called from the Flask-Login library. The function redirect() is called from the Flask library.
    The function url_for() is called from the Flask library
    :return: the redirect function, which is redirecting the user to the home page.
    """
    logout_user()
    print("log this: user logged out")
    return redirect(url_for("home"))


@app.route("/register", methods=["GET", "POST"])
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
        return redirect(url_for("home"))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode(
            "utf8"
        )
        new_user = User(
            username=form.username.data,
            email=form.email.data,
            password=hashed_pw,
        )
        db.session.add(new_user)
        db.session.commit()
        logout_user()
        flash(
            "Your tracker account has been created. You may now login.",
            "success",
        )
        return redirect(url_for("login"))
    return render_template("register.html", active_page="register", form=form)


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


@app.route("/account", methods=["GET"])
def account():
    if current_user.is_authenticated:
        return render_template(
            "account.html", active_page="account", user=current_user
        )
    return redirect(url_for("login.html "))
