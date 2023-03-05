def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello, World!" in response.data

def test_hello(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b'Hello, World!'

def test_main(client):
    from app import app
    print('tuna')
    print(app.name)
    assert app.name == 'app'
    # assert app.app == app.Flask(__name__)
    # with app.app.test_client() as client:
    #     assert client.get('/').status_code == 200
