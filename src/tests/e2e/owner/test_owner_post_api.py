


def test_add_owner_returns_201(client, owner_ex_json):
    response = client.post("/owners/", json=owner_ex_json)
    assert response.status_code == 201
    assert response.json() == owner_ex_json

def test_fails_add_owner_when_data_existed(client, owner_ex_json):
    client.post("/owners/", json=owner_ex_json)
    response = client.post("/owners/", json=owner_ex_json)
    assert response.status_code == 404
    assert response.json() == {'detail': 'existed data'}

def test_fails_add_owner_when_invalid_data_entered(client, invalid_owner_ex_json):
    response = client.post("/owners/", json=invalid_owner_ex_json)
    assert response.status_code == 404
    assert response.json() == {'detail': 'invalid data'}



