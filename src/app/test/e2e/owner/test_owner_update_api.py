def test_update_owner_return_200(client, owner_ex, owner_id):
    response_post_owner = client.post("/owners/", json=owner_ex)
    assert response_post_owner.status_code == 201

    owner_ex["name"] = "nobody"
    response = client.put("/owners/{}".format(owner_id), json=owner_ex)
    assert response.status_code == 200
    assert response.json() == owner_ex


def test_update_owner_not_existed(client, owner_ex, owner_id):
    response = client.put("/owners/{}".format(owner_id), json=owner_ex)
    assert response.status_code == 404
    assert response.json() == {'detail': 'Unavailable data'}
