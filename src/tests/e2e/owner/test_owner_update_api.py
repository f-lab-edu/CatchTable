def test_update_owner_return_200(client, valid_owner_with_password_json, valid_owner_json):
    client.post("/registration/", json=valid_owner_with_password_json)
    valid_owner_json["name"] = "nobody"
    response = client.put("/owners/{}".format(1), json=valid_owner_json)
    assert response.status_code == 200
    assert response.json() == valid_owner_json


def test_fails_update_owner_when_data_not_existed(client, valid_owner_json):
    response = client.put("/owners/{}".format(1), json=valid_owner_json)
    assert response.status_code == 404

