


def test_add_owner_returns_201(client, owner_ex):
    response = client.post("/owners/", json=owner_ex)
    assert response.status_code == 201
    assert response.json() == owner_ex

def test_error_for_duplicated_owner_data(client, owner_ex):
    response_owner_origin = client.post("/owners/", json=owner_ex)
    assert response_owner_origin.status_code == 201

    response = client.post("/owners/", json=owner_ex)
    assert response.status_code == 404
    assert response.json() == {'detail': 'existed data'}

def test_error_if_invalid_owner_data_entered(client, invalid_type_of_owner_ex):
    response = client.post("/owners/", json=invalid_type_of_owner_ex)
    assert response.status_code == 404
    assert response.json() == {'detail': 'invalid data'}



