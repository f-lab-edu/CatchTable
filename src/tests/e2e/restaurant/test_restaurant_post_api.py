def test_add_restaurant_returns_201(client, owner_client_post, restaurant_ex_json):
    response = client.post("/restaurants/?owner_id={}".format(1), json=restaurant_ex_json)
    assert response.status_code == 201
    assert response.json() == restaurant_ex_json


def test_error_for_duplicated_restaurant_data(client, owner_client_post, restaurant_ex_json):
    client.post("/restaurants/?owner_id={}".format(1), json=restaurant_ex_json)
    response = client.post("/restaurants/?owner_id={}".format(1), json=restaurant_ex_json)
    assert response.status_code == 404
    assert response.json() == {'detail': 'existed data'}


def test_error_if_invalid_restaurant_data_entered(client, owner_client_post, invalid_restaurant_ex_json):
    response = client.post("/restaurants/?owner_id={}".format(1), json=invalid_restaurant_ex_json)
    assert response.status_code == 404
    assert response.json() == {'detail': 'invalid data'}