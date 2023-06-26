def test_update_menu_returns_201(client, menu_client_post, menu_ex_json):
    menu_ex_json["menu"]["coffe"] = 5000
    response = client.put("/restaurants/{}/menus/".format(1), json=menu_ex_json)
    assert response.status_code == 200
    assert response.json() == menu_ex_json


def test_update_menu_not_existed(client, restaurant_client_post, menu_ex_json):
    response = client.put("/restaurants/{}/menus/".format(1), json=menu_ex_json)
    assert response.status_code == 404
    assert response.json() == {'detail': 'Unavailable data'}

