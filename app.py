from flask import Flask, render_template, redirect, url_for, flash
from config import Config
import sys

from forms import LoginForm, RegistrationForm

from utils.helpers import clear_form

app = Flask(__name__)
app.config.from_object(Config)

app.config["SECRET_KEY"] = "this-is-a-super-secret-key-wubalubadubdub"

login_name = "Michael Scott"


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", active_page="home", login_name=login_name)


@app.route("/tracker")
def tracker():
    return render_template("tracker.html", active_page="tracker", login_name=login_name)


@app.route("/login", methods=["POST", "GET"])
def login():
    # for now we will redefine login_name here - TODO check login status and set variable as needed
    login_name = ""
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "test@test.com" and form.password.data == "password":
            login_name = form.email.data
            flash("You have been logged in!", "success")
            return redirect(url_for("tracker"))
        else:
            flash("Login Unsuccessful. Please check username and password", "danger")
    return render_template(
        "login.html", active_page="login", login_name=login_name, form=form
    )


@app.route("/logout")
def logout():
    # do things to log out the user
    print("user logged out")
    return redirect(url_for("home"))


@app.route("/register", methods=["GET", "POST"])
def register():
    global login_name
    form = RegistrationForm()
    if form.validate_on_submit():
        login_name = form.data["username"]
        flash("You have been registered!", "success")
        return redirect(url_for("tracker", login_name=login_name))
    return render_template(
        "register.html", active_page="register", login_name=login_name, form=form
    )


@app.route("/clear_form/<form_name>", methods=["POST"])
def clear_form_route(form_name):
    """
    Security considerations using sys module
    Security: If the value of form_name is controlled by user input, you need to make sure that it can't be manipulated to import arbitrary modules or attributes from your system. This could potentially be used to execute arbitrary code on your server or access sensitive data. One way to guard against this is to use a whitelist of allowed form names and check that the requested form is in the whitelist before importing it.
    Namespace collisions: If you have multiple modules that define form classes with the same name, using getattr with sys.modules[__name__] could result in unintended behavior. In this case, it's better to explicitly import the module that defines the form you want to use.
    Readability: Using getattr with sys.modules[__name__] can make your code less readable and harder to follow, especially for developers who are not familiar with your codebase. It's often better to use explicit imports and avoid dynamically importing modules unless it's absolutely necessary.
    """
    print("clicking clear button")
    form_class = getattr(sys.modules[__name__], form_name)
    form = form_class()
    clear_form(form)
    flash("Form cleared", "info")
    return redirect(url_for("register"))


if __name__ == "__main__":
    app.run()
