def test_get_owner_returns_200(client, owner_ex, owner_id):
    response_post_owner = client.post("/owners/", json=owner_ex)
    assert response_post_owner.status_code == 201

    response = client.get("/owners/{}".format(owner_id))
    assert response.status_code == 200
    assert response.json() == owner_ex

def test_get_owner_not_existed(client, owner_id):
    response = client.get("/owners/{}".format(owner_id))
    assert response.status_code == 404
    assert response.json() == {'detail': 'Unavailable data'}

def test_get_owners_list_returns_200(client, owner_ex):
    response_post_owner = client.post("/owners/", json=owner_ex)
    assert response_post_owner.status_code == 201

    response = client.get("/owners/")
    assert response.status_code == 200

def test_get_owners_list_not_existed(client, owner_id):
    response = client.get("/owners/")
    assert response.status_code == 404
    assert response.json() == {'detail': 'Unavailable data'}







