def test_delete_restaurant_return_200(client, owner_id, restaurant_id, restaurant_ex, owner_ex):
    response = client.post("/owners/", json=owner_ex)
    assert response.status_code == 201

    response = client.post("/restaurants/?owner_id={}".format(owner_id), json=restaurant_ex)
    assert response.status_code == 201

    response = client.delete("/restaurants/{}".format(restaurant_id))
    assert response.status_code == 200


def test_delete_restaurant_not_existed(client, restaurant_id):
    response = client.delete("/restaurants/{}".format(restaurant_id))
    assert response.status_code == 404
    assert response.json() == {'detail': 'Unavailable data'}


def test_delete_owner_not_existed_when_already_deleted(client, owner_id, restaurant_id, restaurant_ex, owner_ex):
    response = client.post("/owners/", json=owner_ex)
    assert response.status_code == 201

    response = client.post("/restaurants/?owner_id={}".format(owner_id), json=restaurant_ex)
    assert response.status_code == 201

    response = client.delete("/restaurants/{}".format(restaurant_id))
    assert response.status_code == 200

    response = client.delete("/restaurants/{}".format(restaurant_id))
    assert response.status_code == 404
    assert response.json() == {'detail': 'Unavailable data'}