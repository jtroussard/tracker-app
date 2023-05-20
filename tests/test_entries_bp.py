# somethign wrong with the test data, the entries being added to the database
# between the tests seem to fuck it up and the db context ends up being empty
# after the first test regardless of calling create_entries in test2
def test_all_entry_routes(app, auth, client):
    with app.test_request_context():
        auth.create()
        auth.login()
        auth.create_entries()
    response = client.get("/entry/1")
    assert response.status_code == 200
    response = client.get("/entry/10")
    assert response.status_code == 403
    response = client.get("/entry/99999999999999")
    assert response.status_code == 404
    response = client.get("/entry/1/update")
    assert response.status_code == 200
