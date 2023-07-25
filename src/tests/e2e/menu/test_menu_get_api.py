def test_get_menu_returns_201(client, owner_ex_json, restaurant_ex_json, menu_ex_json):
    client.post("/owners/", json=owner_ex_json)
    client.post("/restaurants/?owner_id={}".format(1), json=restaurant_ex_json)
    client.post("/restaurants/{}/menus/".format(1), json=menu_ex_json)

    response = client.get("/restaurants/{}/menus/".format(1))
    assert response.status_code == 200
    assert response.json() == menu_ex_json


def test_fails_get_menu_when_data_not_existed(client, owner_ex_json, restaurant_ex_json):
    client.post("/owners/", json=owner_ex_json)
    client.post("/restaurants/?owner_id={}".format(1), json=restaurant_ex_json)

    response = client.get("/restaurants/{}/menus/".format(1))
    assert response.status_code == 404
    assert response.json() == {'detail': 'Unavailable data'}