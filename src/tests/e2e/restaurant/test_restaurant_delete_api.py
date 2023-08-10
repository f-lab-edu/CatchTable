def test_delete_restaurant_return_200(client, valid_owner_with_password_json, valid_restaurant_json):
    client.post("/registration/", json=valid_owner_with_password_json)
    client.post("/restaurants/?owner_id={}".format(1), json=valid_restaurant_json)
    response = client.delete("/restaurants/{}".format(1))
    assert response.status_code == 200


def test_fails_delete_restaurant_when_data_not_existed(client):
    response = client.delete("/restaurants/{}".format(1))
    assert response.status_code == 404
    assert response.json() == {'detail': 'Unavailable data'}


