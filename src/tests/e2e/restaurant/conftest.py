import pytest
import json
from tests.unit.restaurant.conftest import *
from tests.e2e.owner.conftest import *

@pytest.fixture
def restaurant_ex_json(restaurant_ex):
    return json.loads(restaurant_ex.json())

@pytest.fixture
def invalid_restaurant_ex_json(invalid_restaurant_ex):
    return json.loads(invalid_restaurant_ex.json())

@pytest.fixture
def restaurant_client_post(client, owner_client_post, restaurant_ex_json):
    client.post("/restaurants/?owner_id={}".format(1), json=restaurant_ex_json)