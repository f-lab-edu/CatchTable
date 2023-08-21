def test_success_add_user_returns_201(client, valid_owner_with_password_json, valid_owner_json):
    response = client.post("/registration/", json=valid_owner_with_password_json)
    assert response.status_code == 201
    assert response.json() == valid_owner_json


def test_fails_add_user_when_user_email_already_existed(client, valid_owner_with_password_json, valid_owner_json):
    client.post("/registration/", json=valid_owner_with_password_json)
    response = client.post("/registration/", json=valid_owner_with_password_json)
    assert response.status_code == 404
