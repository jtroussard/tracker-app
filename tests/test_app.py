def test_hello(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b'Hello, World!'

def test_main(client):
    from app import app
    print('tuna')
    print(app.name)
    assert app.name == 'app'
