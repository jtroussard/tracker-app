from flask import url_for
from flask_login import current_user

from app.models import Member
from tests.utils.registration_data import (
    registration_data_happy_0,
    registration_data_sad_0,
)


def test_route_login(client):
    response = client.get("/login")
    assert response.status_code == 200


def test_route_login_authenticated(app, client, auth):
    with app.test_request_context():
        auth.create()
        auth.login()
        response = client.get("/login")
        redirect_target = response.headers["Location"]
        expected_redirects = [url_for("main.home"), "/"]
        assert response.status_code == 302
        assert current_user.is_authenticated
        assert redirect_target in expected_redirects


def test_route_login_wrong_credentials(client):
    response = client.post(
        url_for("users.login"),
        data={
            "email": "wrongemail@example.com",
            "password": "wrongpassword",
            "remember": False,
        },
    )
    assert b"Login Failed. Please check username/password" in response.data


def test_route_account(client):
    response = client.get("/account")
    assert response.status_code == 302

    redirect_target = response.headers["Location"]
    expected_redirect = url_for("users.login")
    assert redirect_target == expected_redirect


def test_route_account_authenticated(auth, client, app):
    with app.test_request_context():
        auth.create()
        auth.login()
        response = client.get("/account")
        assert response.status_code == 200
        assert current_user.is_authenticated


def test_route_logout(client):
    response = client.get("/logout")
    assert response.status_code == 302

    redirect_target = response.headers["Location"]
    expected_redirects = [url_for("main.home"), "/"]
    assert redirect_target in expected_redirects


def test_route_register(client):
    response = client.get("/register")
    assert response.status_code == 200


def test_route_register_authenticated(app, client, auth):
    with app.test_request_context():
        auth.create()
        auth.login()
        response = client.get("/register")
        redirect_target = response.headers["Location"]
        expected_redirects = [url_for("main.home"), "/"]
        assert response.status_code == 302
        assert current_user.is_authenticated
        assert redirect_target in expected_redirects


def test_registration_function_happy(client, app):
    response = client.post("/register", data=registration_data_happy_0)
    assert response.status_code == 302

    redirect_target = response.headers["Location"]
    expected_redirect = url_for("users.login")
    assert redirect_target == expected_redirect

    with app.app_context():
        assert Member.query.count() == 1
        assert Member.query.first().email == registration_data_happy_0["email"]


def test_registration_function_sad(client, app):
    response = client.post("/register", data=registration_data_sad_0)
    assert response.status_code == 200

    with app.app_context():
        assert Member.query.count() == 0
