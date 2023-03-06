from flask import url_for
from bs4 import BeautifulSoup
from app import app

def test_app_name(client):
    assert app.name == 'app'

# HOME ROUTE
def test_home_page_status_code(client):
    """Test that the home page returns 200 status code."""
    response = client.get('/')
    assert response.status_code == 200

def test_home_page_template(app, client):
    """Test that the home page uses the correct template."""
    response = client.get('/')
    soup = BeautifulSoup(response.data, 'html.parser')
    assert soup.title.string == 'My App'
    assert soup.h1.string == 'Hello World!'

def test_home_page_active_nav(client):
    """Test that the home page has the active class on the correct nav item."""
    response = client.get('/')
    soup = BeautifulSoup(response.data, 'html.parser')
    home_li = soup.find('a', string="Home").find_parent('li')
    assert home_li is not None
    assert 'active' in home_li['class']

def test_home_page_login_name(client, monkeypatch, app):
    """Test that the home page displays the correct login name."""
    response = client.get('/')
    # figure out how to mock app context and set the login name
    assert response.status_code == 200

# TRACKER ROUTE
def test_tracker_page_status_code(client):
    """Test that the tracker page returns 200 status code."""
    response = client.get('/tracker')
    assert response.status_code == 200

def test_tracker_page_template(app, client):
    """Test that the tracker page uses the correct template."""
    response = client.get('/tracker')
    soup = BeautifulSoup(response.data, 'html.parser')
    assert soup.title.string == 'My App'
    assert soup.h1.string == 'Tracker Page!'

def test_tracker_page_active_nav(client):
    """Test that the tracker page has the active class on the correct nav item."""
    response = client.get('/tracker')
    soup = BeautifulSoup(response.data, 'html.parser')
    tracker_li = soup.find('a', string="Tracker").find_parent('li')
    assert tracker_li is not None
    assert 'active' in tracker_li['class']

# LOGIN ROUTE
def test_login_page_status_code(client):
    """Test that the login page returns 200 status code."""
    response = client.get('/login')
    assert response.status_code == 200

def test_login_page_template(app, client):
    """Test that the login page uses the correct template."""
    response = client.get('/login')
    soup = BeautifulSoup(response.data, 'html.parser')
    assert soup.title.string == 'My App'
    assert soup.h1.string == 'Login!'

def test_login_page_active_nav(client):
    """Test that the login page has the active class on the correct nav item."""
    response = client.get('/login')
    soup = BeautifulSoup(response.data, 'html.parser')
    login_li = soup.find('a', string="Login").find_parent('li')
    assert login_li is not None
    assert 'active' in login_li['class']
    
# REGISTER ROUTE
def test_register_page_status_code(client):
    """Test that the register page returns 200 status code."""
    response = client.get('/register')
    assert response.status_code == 200

def test_register_page_template(app, client):
    """Test that the register page uses the correct template."""
    response = client.get('/register')
    soup = BeautifulSoup(response.data, 'html.parser')
    assert soup.title.string == 'My App'
    assert soup.h1.string == 'Register!'

def test_register_page_active_nav(client):
    """Test that the register page has the active class on the correct nav item."""
    response = client.get('/register')
    soup = BeautifulSoup(response.data, 'html.parser')
    register_li = soup.find('a', string="Register").find_parent('li')
    assert register_li is not None
    assert 'active' in register_li['class']

# LOGOUT ROUTE
def test_logout_page_status_code_and_redirect(client):
    """Test that the logout page returns 302 status code and redirects to the correct page."""
    with app.app_context():
        response = client.get('/logout')
        assert response.status_code == 302
        expected_location = url_for('home', _external=True)
        assert f"{app.config['BASE_URL']}{response.location}" == expected_location
        response = client.get('/logout', follow_redirects=True)
        assert response.status_code == 200
        assert b'Hello World!' in response.data
