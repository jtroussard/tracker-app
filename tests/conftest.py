import pytest
from datetime import datetime, date

from app import create_app, db, bcrypt
from app.config.testing_config import TestingConfig
from app.models import Member

from tests.utils.entry_objects import (
    entry_object_0,
    entry_object_1,
    entry_object_3,
    entry_object_4,
)


class AuthActions:
    def __init__(
        self, client, email="worlds-most-famous-spy@example.com", password="password123"
    ):
        self.client = client
        self.email = email
        self.password = password

    def create(self):
        with self.client.application.app_context():
            member = Member(
                id=1,
                username="archersterling",
                first_name="Archer",
                middle_name="D",
                last_name="Sterling",
                date_of_birth=date(1990, 1, 1),
                location="New York",
                email="worlds-most-famous-spy@example.com",
                image_file="default.jpg",
                password=bcrypt.generate_password_hash("password123").decode("utf8"),
                joined_date=datetime.utcnow(),
                active_record=True,
                entry=[],
            )
            db.session.add(member)
            db.session.commit()

    def create_entries(self):
        with self.client.application.app_context():
            db.session.add(entry_object_0)
            db.session.add(entry_object_1)
            db.session.add(entry_object_3)
            db.session.add(entry_object_4)
            db.session.commit()

    # def create_double_email(self):
    #     with self.client.application.app_context():
    #         member = Member(
    #         id=2,
    #         username="archersterling2",
    #         first_name="Archer",
    #         middle_name="D",
    #         last_name="Sterling",
    #         date_of_birth=date(1990, 1, 1),
    #         location="New York",
    #         email="worlds-most-famous-spy@example.com",
    #         image_file="default.jpg",
    #         password= bcrypt.generate_password_hash('password123').decode("utf8"),
    #         joined_date=datetime.utcnow(),
    #         active_record=True,
    #         entry=[],
    #     )
    #         db.session.add(member)
    #         db.session.commit()

    def login(self):
        return self.client.post(
            "/login", data={"email": self.email, "password": self.password}
        )

    def logout(self):
        return self.client.get("/logout")


@pytest.fixture()
def app():
    app = create_app(TestingConfig)

    with app.app_context():
        db.create_all()

    yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture
def auth(client):
    return AuthActions(client)
