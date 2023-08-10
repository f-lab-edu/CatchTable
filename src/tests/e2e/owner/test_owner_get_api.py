def test_get_owner_returns_200(client, valid_owner_with_password_json, valid_owner_json):
    client.post("/registration/", json=valid_owner_with_password_json)
    response = client.get("/owners/{}".format(1))
    assert response.status_code == 200
    assert response.json() == valid_owner_json

def test_fails_get_owner_when_data_not_existed(client):
    response = client.get("/owners/{}".format(1))
    assert response.status_code == 404
    assert response.json() == {'detail': 'Unavailable data'}

def test_get_owners_list_returns_200(client, valid_owner_with_password_json, valid_owner_json):
    client.post("/registration/", json=valid_owner_with_password_json)
    response = client.get("/owners/")
    assert response.status_code == 200

def test_fails_get_owners_when_list_not_existed(client):
    response = client.get("/owners/")
    assert response.status_code == 404
    assert response.json() == {'detail': 'Unavailable data'}







