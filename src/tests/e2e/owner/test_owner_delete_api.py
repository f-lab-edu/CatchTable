def test_delete_owner_return_200(client, owner_ex_json):
    client.post("/owners/", json=owner_ex_json)
    response = client.delete("/owners/{}".format(1))
    assert response.status_code == 200


def test_fails_delete_owner_when_data_not_existed(client):
    response = client.delete("/owners/{}".format(2))
    assert response.status_code == 404
    assert response.json() == {'detail': 'Unavailable data'}



