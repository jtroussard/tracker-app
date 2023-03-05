import pytest
import os
import sys

# Set the project root directory
root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Add the project root directory to the system path
sys.path.insert(0, root)

from app import app as flask_app

@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()
