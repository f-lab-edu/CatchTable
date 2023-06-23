def test_get_restaurant_returns_200(client, owner_id, restaurant_id, restaurant_ex, owner_ex):
    response = client.post("/owners/", json=owner_ex)
    assert response.status_code == 201

    response = client.post("/restaurants/?owner_id={}".format(owner_id), json=restaurant_ex)
    assert response.status_code == 201

    response = client.get("/restaurants/{}".format(restaurant_id))
    assert response.status_code == 200
    assert response.json() == restaurant_ex


def test_get_restaurant_not_existed(client, restaurant_id):
    response = client.get("/restaurants/{}".format(restaurant_id))
    assert response.status_code == 404
    assert response.json() == {'detail': 'Unavailable data'}


def test_get_restaurants_list_returns_200(client, owner_id, restaurant_id, restaurant_ex, owner_ex):
    response = client.post("/owners/", json=owner_ex)
    assert response.status_code == 201

    response = client.post("/restaurants/?owner_id={}".format(owner_id), json=restaurant_ex)
    assert response.status_code == 201

    restaurant_ex2 = restaurant_ex.copy()
    restaurant_ex2["name"] = "nobody_restaurant"
    response = client.post("/restaurants/?owner_id={}".format(owner_id), json=restaurant_ex2)
    assert response.status_code == 201

    response = client.get("/restaurants/?filter={}&value={}".format("city", "seoul"))
    assert response.status_code == 200
    assert response.json() == [restaurant_ex, restaurant_ex2]


def test_get_restaurants_list_not_existed(client):
    response = client.get("/restaurants/?filter={}&value={}".format("city", "seoul"))
    assert response.status_code == 404
    assert response.json() == {'detail': 'Unavailable data'}


