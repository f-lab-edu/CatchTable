def test_get_restaurant_returns_200(client, valid_owner_with_password_json, valid_restaurant_json):
    client.post("/registration/", json=valid_owner_with_password_json)
    client.post("/restaurants/?owner_id={}".format(1), json=valid_restaurant_json)
    response = client.get("/restaurants/{}".format(1))
    assert response.status_code == 200
    assert response.json() == valid_restaurant_json


def test_fails_get_restaurant_when_data_not_existed(client):
    response = client.get("/restaurants/{}".format(1))
    assert response.status_code == 404
    assert response.json() == {'detail': 'Unavailable data'}


def test_get_restaurants_list_returns_200(client, valid_owner_with_password_json, valid_restaurant_json):
    client.post("/registration/", json=valid_owner_with_password_json)
    client.post("/restaurants/?owner_id={}".format(1), json=valid_restaurant_json)
    response = client.get("/restaurants/?filter={}&value={}".format("city", "seoul"))
    assert response.status_code == 200
    assert response.json() == [valid_restaurant_json]


def test_fails_get_restaurants_list_when_data_not_existed(client):
    response = client.get("/restaurants/?filter={}&value={}".format("city", "seoul"))
    assert response.status_code == 404
    assert response.json() == {'detail': 'Unavailable data'}


