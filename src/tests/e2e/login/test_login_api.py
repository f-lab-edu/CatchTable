def test_success_user_login_returns_200(client, valid_owner_with_password_json):
    client.post("/registration/", json=valid_owner_with_password_json)
    response = client.post("/login/", json=valid_owner_with_password_json)
    assert response.status_code == 200


def test_fails_user_login_when_user_email_not_existed(client, valid_owner_with_password_json):
    response = client.post("/login/", json=valid_owner_with_password_json)
    assert response.status_code == 404
    assert response.json() == {'detail': 'email not existed'}


def test_fails_user_login_when_passowrd_not_matched(client, valid_owner_with_password_json, valid_owner_json):
    client.post("/registration/", json=valid_owner_with_password_json)
    valid_owner_with_password_json['hashed_password'] = '2222'
    response = client.post("/login/", json=valid_owner_with_password_json)
    assert response.status_code == 404
    assert response.json() == {'detail': 'password not matched'}