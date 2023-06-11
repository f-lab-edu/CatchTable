def test_update_restaurant_returns_200(client, owner_id, restaurant_id, restaurant_ex, owner_ex):
    response = client.post("/owners/", json=owner_ex)
    assert response.status_code == 201

    response = client.post("/restaurants/?owner_id={}".format(owner_id), json=restaurant_ex)
    assert response.status_code == 201

    restaurant_ex["name"] = "nobody"
    response = client.put("/restaurants/{}".format(restaurant_id), json=restaurant_ex)
    assert response.status_code == 200
    assert response.json() == restaurant_ex


def test_update_restaurant_not_existed(client, restaurant_id, restaurant_ex):
    response = client.put("/restaurants/{}".format(restaurant_id), json=restaurant_ex)
    assert response.status_code == 404
    assert response.json() == {'detail': 'Unavailable data'}