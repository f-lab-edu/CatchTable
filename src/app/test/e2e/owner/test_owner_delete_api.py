def test_delete_owner_return_200(client, owner_ex, owner_id):
    response_post_owner = client.post("/owners/", json=owner_ex)
    assert response_post_owner.status_code == 201

    response = client.delete("/owners/{}".format(owner_id))
    assert response.status_code == 200


def test_delete_owner_not_existed(client, owner_id):
    response = client.get("/owners/{}".format(owner_id))
    assert response.status_code == 404
    assert response.json() == {'detail': 'Unavailable data'}


def test_delete_owner_not_existed_when_already_deleted(client, owner_ex,owner_id):
    response_post_owner = client.post("/owners/", json=owner_ex)
    assert response_post_owner.status_code == 201

    response = client.delete("/owners/{}".format(owner_id))
    assert response.status_code == 200

    response = client.get("/owners/{}".format(owner_id))
    assert response.status_code == 404
    assert response.json() == {'detail': 'Unavailable data'}