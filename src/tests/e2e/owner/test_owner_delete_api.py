def test_delete_owner_return_200(client, owner_client_post, owner_ex_json):
    response = client.delete("/owners/{}".format(1))
    assert response.status_code == 200


def test_delete_owner_not_existed(client, owner_client_post):
    response = client.delete("/owners/{}".format(2))
    assert response.status_code == 404
    assert response.json() == {'detail': 'Unavailable data'}


# def test_delete_owner_without_authentication(client, owner_client_post):
#     response = client.delete("/owners/{}".format(1))
#     assert response.status_code == 403
#     assert response.json() == {'detail': 'Access denied'}

