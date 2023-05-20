def test_route_index(client):
    response = client.get("/")
    assert response.status_code == 200


def test_route_home(client):
    response = client.get("/home")
    assert response.status_code == 200
