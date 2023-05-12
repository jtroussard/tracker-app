from flask import Flask

from app import db, login_manager, migrate


def test_create_app(app):
    assert isinstance(app, Flask)
    assert app.config["TESTING"] is True


def test_login_manager(app):
    with app.app_context():
        assert login_manager.login_view == "users.login"


def test_migrate(app):
    with app.app_context():
        assert migrate.db is db


def test_register_filters(app):
    with app.app_context():
        assert "get_username_filter" in app.jinja_env.filters
        assert "get_month_name" in app.jinja_env.filters
        assert "get_user_fullname" in app.jinja_env.filters
        assert "get_pretty_date" in app.jinja_env.filters


def test_blueprints(app):
    with app.app_context():
        assert "users" in app.blueprints
        assert "entries" in app.blueprints
        assert "main" in app.blueprints
