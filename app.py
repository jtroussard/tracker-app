from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from config import Config
import sys

from forms import LoginForm, RegistrationForm, TrackerEntryForm
from datetime import date, datetime

from utils.helpers import clear_form

db = SQLAlchemy()

app = Flask(__name__)
app.config.from_object(Config)
app.config["SECRET_KEY"] = "this-is-a-super-secret-key-wubalubadubdub"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

db.init_app(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default="default.jpg")
    password = db.Column(db.String(60), nullable=False)
    entry = db.relationship("TrackerEntry", backref="author", lazy="select")

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class TrackerEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow
    )  # pass the function not the return value
    time_of_day = db.Column(db.String(20))
    mood = db.Column(db.String(20))
    status = db.Column(db.String(20))
    weight = db.Column(db.Float(), nullable=False)
    measurement_waist = db.Column(db.Float())
    keto = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __repr__(self):
        return f"TrackerEntry('{self.date}', '{self.weight}')"


login_name = "Michael Scott"

test_entries = [
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
    return render_template("home.html", active_page="home", login_name=login_name)


@app.route("/tracker", methods=["GET", "POST"])
def tracker():
    form = TrackerEntryForm()
    if form.validate_on_submit():
        date = form.date.data
        time_of_day = form.time_of_day.data
        mood = form.mood.data
        status = form.status.data
        weight = form.weight.data
        measurement_waist = form.measurement_waist.data
        keto = form.keto.data
        print("success")
        flash(f"You have submitted an entry", "success")
        return render_template(
            "tracker.html",
            active_page="tracker",
            login_name=login_name,
            entries=test_entries,
            form=form,
        )
    return render_template(
        "tracker.html",
        active_page="tracker",
        login_name=login_name,
        entries=test_entries,
        form=form,
    )


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
