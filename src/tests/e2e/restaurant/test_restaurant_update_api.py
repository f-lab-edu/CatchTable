def test_success_update_restaurant_returns_200(client, valid_owner_with_password_json, valid_restaurant_json):
    client.post("/registration/", json=valid_owner_with_password_json)
    client.post("/restaurants/?owner_id={}".format(1), json=valid_restaurant_json)

    valid_restaurant_json["name"] = "nobody"
    response = client.put("/restaurants/{}".format(1), json=valid_restaurant_json)
    assert response.status_code == 200
    assert response.json() == valid_restaurant_json


def test_fails_update_restaurant_when_data_not_existed(client, valid_restaurant_json):
    response = client.put("/restaurants/{}".format(1), json=valid_restaurant_json)
    assert response.status_code == 404
    assert response.json() == {'detail': 'Unavailable data'}