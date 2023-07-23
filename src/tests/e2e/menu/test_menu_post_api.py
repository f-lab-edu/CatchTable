
def test_add_menu_returns_201(client, owner_ex_json, restaurant_ex_json, menu_ex_json):
    client.post("/owners/", json=owner_ex_json)
    client.post("/restaurants/?owner_id={}".format(1), json=restaurant_ex_json)
    response = client.post("/restaurants/{}/menus/".format(1), json=menu_ex_json)
    assert response.status_code == 201
    assert response.json() == menu_ex_json

