"""A blueprint module for the main page of the website.

This module provides a route for the home page.

Routes:
    home(): Renders the home page.
"""
import logging
from flask import Blueprint, render_template, current_app

LOG = logging.getLogger(__name__)

main = Blueprint("main", __name__)


@main.route("/")
@main.route("/home")
def home():
    """Renders the home page."""
    LOG.info("Logging is working")
    return render_template("home.html", active_page="home")
