"""A blueprint module for the main page of the website.

This module provides a route for the home page.

Routes:
    home(): Renders the home page.
"""

from flask import Blueprint, render_template

main = Blueprint("main", __name__)


@main.route("/")
@main.route("/home")
def home():
    """Renders the home page."""
    return render_template("home.html", active_page="home")
