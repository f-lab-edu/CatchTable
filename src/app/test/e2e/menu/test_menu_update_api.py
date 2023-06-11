def test_update_menu_returns_201(client, owner_id, restaurant_id, owner_ex, restaurant_ex, menu_ex):
    response_owner = client.post("/owners/", json=owner_ex)
    assert response_owner.status_code == 201

    response_restaurant = client.post("/restaurants/?owner_id={}".format(owner_id), json=restaurant_ex)
    assert response_restaurant.status_code == 201

    response = client.post("/restaurants/{}/menus/".format(restaurant_id), json=menu_ex)
    assert response.status_code == 201

    menu_ex["menu"]["coffe"] = 5000
    response = client.put("/restaurants/{}/menus/".format(restaurant_id), json=menu_ex)
    assert response.status_code == 200
    assert response.json() == menu_ex


def test_update_menu_not_existed(client, owner_id, restaurant_id, owner_ex, restaurant_ex, menu_ex):
    response_owner = client.post("/owners/", json=owner_ex)
    assert response_owner.status_code == 201

    response_restaurant = client.post("/restaurants/?owner_id={}".format(owner_id), json=restaurant_ex)
    assert response_restaurant.status_code == 201

    response = client.put("/restaurants/{}/menus/".format(restaurant_id), json=menu_ex)
    assert response.status_code == 404
    assert response.json() == {'detail': 'Unavailable data'}

