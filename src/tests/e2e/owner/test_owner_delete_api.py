def test_delete_owner_return_200(client, valid_owner_with_password_json):
    client.post("/registration/", json=valid_owner_with_password_json)
    response = client.delete("/owners/{}".format(1))
    assert response.status_code == 200


def test_fails_delete_owner_when_data_not_existed(client):
    response = client.delete("/owners/{}".format(2))
    assert response.status_code == 404




