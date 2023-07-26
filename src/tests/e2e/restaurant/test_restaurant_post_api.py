def test_add_restaurant_returns_201(client, owner_ex_json, restaurant_ex_json):
    client.post("/owners/", json=owner_ex_json)
    response = client.post("/restaurants/?owner_id={}".format(1), json=restaurant_ex_json)
    assert response.status_code == 201
    assert response.json() == restaurant_ex_json


def test_fails_add_restaurant_when_data_duplicated(client, owner_ex_json, restaurant_ex_json):
    client.post("/owners/", json=owner_ex_json)
    client.post("/restaurants/?owner_id={}".format(1), json=restaurant_ex_json)
    response = client.post("/restaurants/?owner_id={}".format(1), json=restaurant_ex_json)
    assert response.status_code == 404
    assert response.json() == {'detail': 'existed data'}


def test_fails_when_invalid_data_entered(client, owner_ex_json, invalid_restaurant_ex_json):
    client.post("/owners/", json=owner_ex_json)
    response = client.post("/restaurants/?owner_id={}".format(1), json=invalid_restaurant_ex_json)
    assert response.status_code == 404
    assert response.json() == {'detail': 'invalid data'}