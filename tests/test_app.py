from bs4 import BeautifulSoup

def test_app_name(client):
    from app import app
    assert app.name == 'app'

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
    
