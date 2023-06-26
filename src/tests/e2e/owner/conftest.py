import pytest
import json
from tests.unit.owner.conftest import *

@pytest.fixture
def owner_ex_json(owner_ex):
    return json.loads(owner_ex.json())

@pytest.fixture
def invalid_owner_ex_json(invalid_owner_ex):
    return json.loads(invalid_owner_ex.json())

@pytest.fixture
def owner_client_post(client, owner_ex_json):
    client.post("/owners/", json=owner_ex_json)