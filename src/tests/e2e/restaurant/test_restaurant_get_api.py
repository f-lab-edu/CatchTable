def test_get_restaurant_returns_200(client, restaurant_client_post, restaurant_ex_json):
    response = client.get("/restaurants/{}".format(1))
    assert response.status_code == 200
    assert response.json() == restaurant_ex_json


def test_get_restaurant_not_existed(client):
    response = client.get("/restaurants/{}".format(1))
    assert response.status_code == 404
    assert response.json() == {'detail': 'Unavailable data'}


def test_get_restaurants_list_returns_200(client, restaurant_client_post, restaurant_ex_json):
    response = client.get("/restaurants/?filter={}&value={}".format("city", "seoul"))
    assert response.status_code == 200
    assert response.json() == [restaurant_ex_json]


def test_get_restaurants_list_not_existed(client, owner_client_post):
    response = client.get("/restaurants/?filter={}&value={}".format("city", "seoul"))
    assert response.status_code == 404
    assert response.json() == {'detail': 'Unavailable data'}


