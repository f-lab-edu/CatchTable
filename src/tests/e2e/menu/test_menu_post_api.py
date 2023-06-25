
def test_add_menu_returns_201(client, restaurant_client_post, menu_ex_json):
    response = client.post("/restaurants/{}/menus/".format(1), json=menu_ex_json)
    assert response.status_code == 201
    assert response.json() == menu_ex_json

