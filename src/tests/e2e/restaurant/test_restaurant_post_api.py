def test_add_restaurant_returns_201(client, valid_owner_with_password_json, valid_restaurant_json):
    client.post("/registration/", json=valid_owner_with_password_json)
    response = client.post("/restaurants/?owner_id={}".format(1), json=valid_restaurant_json)
    assert response.status_code == 201
    assert response.json() == valid_restaurant_json


def test_fails_add_restaurant_when_data_duplicated(client, valid_owner_with_password_json, valid_restaurant_json):
    client.post("/registration/", json=valid_owner_with_password_json)
    client.post("/restaurants/?owner_id={}".format(1), json=valid_restaurant_json)
    response = client.post("/restaurants/?owner_id={}".format(1), json=valid_restaurant_json)
    assert response.status_code == 404



def test_fails_when_invalid_data_entered(client, valid_owner_with_password_json, invalid_restaurant_json):
    client.post("/registration/", json=valid_owner_with_password_json)
    response = client.post("/restaurants/?owner_id={}".format(1), json=invalid_restaurant_json)
    assert response.status_code == 404
