def test_add_restaurant_returns_201(client, owner_id, restaurant_ex, owner_ex):
    response_owner = client.post("/owners/", json=owner_ex)
    assert response_owner.status_code == 201

    response = client.post("/restaurants/?owner_id={}".format(owner_id), json=restaurant_ex)
    assert response.status_code == 201
    assert response.json() == restaurant_ex


def test_error_for_duplicated_restaurant_data(client, owner_id, owner_ex, restaurant_ex):
    response_owner = client.post("/owners/", json=owner_ex)
    assert response_owner.status_code == 201

    response = client.post("/restaurants/?owner_id={}".format(owner_id), json=restaurant_ex)
    assert response.status_code == 201
    assert response.json() == restaurant_ex

    response = client.post("/restaurants/?owner_id={}".format(owner_id), json=restaurant_ex)
    assert response.status_code == 404
    assert response.json() == {'detail': 'existed data'}


def test_error_if_invalid_restaurant_data_entered(client, owner_id, owner_ex, invalid_type_of_restaurant_ex):
    response_owner = client.post("/owners/", json=owner_ex)
    assert response_owner.status_code == 201

    response = client.post("/restaurants/?owner_id={}".format(owner_id), json=invalid_type_of_restaurant_ex)
    assert response.status_code == 404
    assert response.json() == {'detail': 'invalid data'}