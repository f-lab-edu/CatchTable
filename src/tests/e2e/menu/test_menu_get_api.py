def test_get_menu_returns_201(client, menu_client_post, menu_ex_json):
    response = client.get("/restaurants/{}/menus/".format(1))
    assert response.status_code == 200
    assert response.json() == menu_ex_json


def test_get_menu_not_existed(client, restaurant_client_post):
    response = client.get("/restaurants/{}/menus/".format(1))
    assert response.status_code == 404
    assert response.json() == {'detail': 'Unavailable data'}