def test_get_menu_returns_201(client, valid_owner_with_password_json, valid_restaurant_json, valid_menu_json):
    client.post("/registration/", json=valid_owner_with_password_json)
    client.post("/restaurants/?owner_id={}".format(1), json=valid_restaurant_json)
    client.post("/restaurants/{}/menus/".format(1), json=valid_menu_json)

    response = client.get("/restaurants/{}/menus/".format(1))
    assert response.status_code == 200
    assert response.json() == valid_menu_json


def test_fails_get_menu_when_data_not_existed(client, valid_owner_with_password_json, valid_restaurant_json):
    client.post("/registration/", json=valid_owner_with_password_json)
    client.post("/restaurants/?owner_id={}".format(1), json=valid_restaurant_json)

    response = client.get("/restaurants/{}/menus/".format(1))
    assert response.status_code == 404
