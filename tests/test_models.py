from app import models
from tests.utils.member_objects import member_data_0
from tests.utils.entry_objects import (
    entry_object_0,
    no_load_entry_object_0,
    no_load_entry_object_2,
    no_load_entry_object_3,
)


def test_load_user(app, auth):
    with app.test_request_context():
        auth.create()
        user = models.load_user(1)
        assert user.username == "archersterling"
        assert user.email == "worlds-most-famous-spy@example.com"
        assert user.image_file == "default.jpg"


def test_repr_Member():
    assert member_data_0.__repr__() == "Member(archersterling)"


def test_eq_Entry(app, auth):
    assert no_load_entry_object_2 == no_load_entry_object_0


def test_not_eq_Entry(app, auth):
    assert no_load_entry_object_3 != no_load_entry_object_0


def test_not_entry_object_Entry():
    not_an_entry = "danger zone"
    assert not_an_entry != entry_object_0


def test_repr_entry():
    expected_entry = no_load_entry_object_0
    expected_repr = "Entry('5: Author=1, Weight=250, Active='True')"
    assert repr(expected_entry) == expected_repr
