import pytest
from app.domain.schemas import Menu
from tests.unit.restaurant.conftest import *
from app.service_layer.services import menu

@pytest.fixture
def menu_ex():
    return Menu(menu={
                    'steak': 30000,
                    'pasta': 18000,
                    'coke': 4000
                    })

@pytest.fixture
def create_menu(override_get_uow, create_restaurant, menu_ex):
    menu.add_menu(1, menu_ex, override_get_uow)
