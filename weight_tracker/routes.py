import sys
from datetime import date

from flask import render_template, redirect, url_for, flash
from weight_tracker import app
from weight_tracker.forms import LoginForm, RegistrationForm, TrackerEntryForm
from weight_tracker.utils.helpers import clear_form

LOGIN_NAME = "Michael Scott"
TEST_ENTRIES = [
    {
        "date": date(2022, 1, 1),
        "time_of_day": "morning",
        "mood": "happy",
        "status": "good",
        "weight": 150.5,
        "measurement_waist": 28.5,
        "keto": 4,
    },
    {
        "date": date(2022, 1, 2),
        "time_of_day": "afternoon",
        "mood": "tired",
        "status": "okay",
        "weight": 148.8,
        "measurement_waist": 28.0,
        "keto": 3,
    },
    {
        "date": date(2022, 1, 3),
        "time_of_day": "evening",
        "mood": "grumpy",
        "status": "bad",
        "weight": 151.2,
        "measurement_waist": 29.0,
        "keto": 2,
    },
]


@app.route("/")
@app.route("/home")
def home():
    """
    The function home() returns the rendered template "home.html" with the
    variables active_page and LOGIN_NAME
    :return: The home.html file is being returned.
    """
    return render_template("home.html", active_page="home", login_name=LOGIN_NAME)


@app.route("/tracker", methods=["GET", "POST"])
def tracker():
    """
    The function tracker() is called when the user visits the /tracker route.
    :return: The tracker page is being returned.
    """
    form = TrackerEntryForm()
    if form.validate_on_submit():
        date = form.date.data
        time_of_day = form.time_of_day.data
        mood = form.mood.data
        status = form.status.data
        weight = form.weight.data
        measurement_waist = form.measurement_waist.data
        keto = form.keto.data
        print(f"success: {date}, {time_of_day}, {mood}, {status}, {weight}, {measurement_waist}, {keto}")
        flash("You have submitted an entry", "success")
        return render_template(
            "tracker.html",
            active_page="tracker",
            login_name=LOGIN_NAME,
            entries=TEST_ENTRIES,
            form=form,
        )
    return render_template(
        "tracker.html",
        active_page="tracker",
        login_name=LOGIN_NAME,
        entries=TEST_ENTRIES,
        form=form,
    )


@app.route("/login", methods=["POST", "GET"])
def login():
    """
    If the form is submitted and the email and password are correct, then the
    user is logged in and redirected to the tracker page
    :return: The login.html template is being returned.
    """
    # for now we will redefine login_name here - TODO check login status and set variable as needed
    name = ""
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "test@test.com" and form.password.data == "password":
            name = form.email.data
            flash("You have been logged in!", "success")
            return redirect(url_for("tracker"))
        flash("Login Unsuccessful. Please check username and password", "danger")
    return render_template(
        "login.html", active_page="login", login_name=name, form=form
    )


@app.route("/logout")
def logout():
    """
    Not implemented yet.
    :return: a redirect to the home page.
    """
    # do things to log out the user
    print("user logged out")
    return redirect(url_for("home"))


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    If the form is valid, set the global variable `LOGIN_NAME` to the username
    entered in the form, flash a success message, and redirect to the tracker
    page. Otherwise, render the register page with the form.
    :return: the rendered template for the register page.
    """
    global LOGIN_NAME
    form = RegistrationForm()
    if form.validate_on_submit():
        LOGIN_NAME = form.data["username"]
        flash("You have been registered!", "success")
        return redirect(url_for("tracker", login_name=LOGIN_NAME))
    return render_template(
        "register.html", active_page="register", login_name=LOGIN_NAME, form=form
    )


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
