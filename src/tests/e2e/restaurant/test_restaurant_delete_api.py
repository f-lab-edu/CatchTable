def test_delete_restaurant_return_200(client, restaurant_client_post):
    response = client.delete("/restaurants/{}".format(1))
    assert response.status_code == 200


def test_delete_restaurant_returns_error_when_not_existed(client):
    response = client.delete("/restaurants/{}".format(1))
    assert response.status_code == 404
    assert response.json() == {'detail': 'Unavailable data'}


