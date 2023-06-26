import pytest
import json
from tests.unit.menu.conftest import *
from tests.e2e.restaurant.conftest import *

@pytest.fixture
def menu_ex_json(menu_ex):
    return json.loads(menu_ex.json())

@pytest.fixture
def invalid_menu_ex_json(invalid_menu_ex):
    return json.loads(invalid_menu_ex.json())

@pytest.fixture
def menu_client_post(client, restaurant_client_post, menu_ex_json):
    client.post("/restaurants/{}/menus/".format(1), json=menu_ex_json)
