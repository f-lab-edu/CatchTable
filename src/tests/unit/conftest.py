import pytest
from tests.unit.owner.conftest import *
from tests.unit.restaurant.conftest import *
from tests.unit.menu.conftest import *
from app.service_layer.services import owner, restaurant, menu


@pytest.fixture
def create_owner(owner_ex, override_get_uow):
    owner.add_owner(owner_ex, override_get_uow)


@pytest.fixture
def create_restaurant(create_owner, restaurant_ex, override_get_uow):
    restaurant.add_restaurant(1, restaurant_ex, override_get_uow)


@pytest.fixture
def create_menu(override_get_uow, create_restaurant, menu_ex):
    menu.add_menu(1, menu_ex, override_get_uow)


