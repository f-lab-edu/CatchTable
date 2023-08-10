
def test_add_menu_returns_201(client, valid_owner_with_password_json, valid_restaurant_json, valid_menu_json):
    client.post("/registration/", json=valid_owner_with_password_json)
    client.post("/restaurants/?owner_id={}".format(1), json=valid_restaurant_json)
    response = client.post("/restaurants/{}/menus/".format(1), json=valid_menu_json)
    assert response.status_code == 201
    assert response.json() == valid_menu_json

