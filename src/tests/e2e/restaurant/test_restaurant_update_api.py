def test_update_restaurant_returns_200(client, owner_ex_json, restaurant_ex_json):
    client.post("/owners/", json=owner_ex_json)
    client.post("/restaurants/?owner_id={}".format(1), json=restaurant_ex_json)

    restaurant_ex_json["name"] = "nobody"
    response = client.put("/restaurants/{}".format(1), json=restaurant_ex_json)
    assert response.status_code == 200
    assert response.json() == restaurant_ex_json


def test_fails_update_restaurant_when_data_not_existed(client, restaurant_ex_json):
    response = client.put("/restaurants/{}".format(1), json=restaurant_ex_json)
    assert response.status_code == 404
    assert response.json() == {'detail': 'Unavailable data'}