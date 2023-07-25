def test_update_owner_return_200(client, owner_ex_json):
    client.post("/owners/", json=owner_ex_json)
    owner_ex_json["name"] = "nobody"
    response = client.put("/owners/{}".format(1), json=owner_ex_json)
    assert response.status_code == 200
    assert response.json() == owner_ex_json


def test_fails_update_owner_when_data_not_existed(client, owner_ex_json):
    response = client.put("/owners/{}".format(1), json=owner_ex_json)
    assert response.status_code == 404
    assert response.json() == {'detail': 'Unavailable data'}
