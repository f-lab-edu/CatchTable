

def test_add_owner_returns_201(client, owner_ex):
    result = client.post("/owners/", data=owner_ex)
    assert result == owner_ex



