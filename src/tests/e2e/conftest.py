import pytest
from tests.e2e.owner.conftest import *
from tests.e2e.restaurant.conftest import *
from tests.e2e.menu.conftest import *


@pytest.fixture
def owner_client_post(client, owner_ex_json):
    client.post("/owners/", json=owner_ex_json)


@pytest.fixture
def restaurant_client_post(client, owner_client_post, restaurant_ex_json):
    client.post("/restaurants/?owner_id={}".format(1), json=restaurant_ex_json)


@pytest.fixture
def menu_client_post(client, restaurant_client_post, menu_ex_json):
    client.post("/restaurants/{}/menus/".format(1), json=menu_ex_json)