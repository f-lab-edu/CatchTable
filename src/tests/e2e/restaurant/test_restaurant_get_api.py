def test_get_restaurant_returns_200(client, owner_ex_json, restaurant_ex_json):
    client.post("/owners/", json=owner_ex_json)
    client.post("/restaurants/?owner_id={}".format(1), json=restaurant_ex_json)
    response = client.get("/restaurants/{}".format(1))
    assert response.status_code == 200
    assert response.json() == restaurant_ex_json


def test_fails_get_restaurant_when_data_not_existed(client):
    response = client.get("/restaurants/{}".format(1))
    assert response.status_code == 404
    assert response.json() == {'detail': 'Unavailable data'}


def test_get_restaurants_list_returns_200(client, owner_ex_json, restaurant_ex_json):
    client.post("/owners/", json=owner_ex_json)
    client.post("/restaurants/?owner_id={}".format(1), json=restaurant_ex_json)
    response = client.get("/restaurants/?filter={}&value={}".format("city", "seoul"))
    assert response.status_code == 200
    assert response.json() == [restaurant_ex_json]


def test_fails_get_restaurants_list_when_data_not_existed(client):
    response = client.get("/restaurants/?filter={}&value={}".format("city", "seoul"))
    assert response.status_code == 404
    assert response.json() == {'detail': 'Unavailable data'}


