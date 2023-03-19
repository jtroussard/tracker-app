"""Main blueprint module"""
from flask import Blueprint, render_template

main = Blueprint("main", __name__)


@main.route("/")
@main.route("/home")
def home():
    """
    The function home() returns the rendered template "home.html" with the
    variables active_page and
    :return: The home.html file is being returned.
    """
    return render_template("home.html", active_page="home")
