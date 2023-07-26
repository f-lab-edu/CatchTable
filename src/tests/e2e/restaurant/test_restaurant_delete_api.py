def test_delete_restaurant_return_200(client, owner_ex_json, restaurant_ex_json):
    client.post("/owners/", json=owner_ex_json)
    client.post("/restaurants/?owner_id={}".format(1), json=restaurant_ex_json)
    response = client.delete("/restaurants/{}".format(1))
    assert response.status_code == 200


def test_fails_delete_restaurant_when_data_not_existed(client):
    response = client.delete("/restaurants/{}".format(1))
    assert response.status_code == 404
    assert response.json() == {'detail': 'Unavailable data'}


