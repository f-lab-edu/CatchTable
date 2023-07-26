import pytest
import app.domain.model as model
from app.service_layer import errors
from app.service_layer.services import owner, restaurant, menu
from tests.unit.restaurant.test_restaurant_services import add_restaurant

def add_menu(override_get_uow, owner_ex, restaurant_ex, menu_ex):
    owner.add_owner(owner_ex, override_get_uow)
    restaurant.add_restaurant(1, restaurant_ex, override_get_uow)
    menu.add_menu(1, menu_ex, override_get_uow)

def test_success_add_menu(override_get_uow, owner_ex, restaurant_ex, menu_ex):
    add_menu(override_get_uow, owner_ex, restaurant_ex, menu_ex)
    assert override_get_uow.batches.get(model.Menu, 1) is not None

def test_fails_add_menu_when_restaurant_not_found(override_get_uow, menu_ex):
    with pytest.raises(errors.NotFoundException) as error:
        menu.add_menu(1, menu_ex, override_get_uow)
    assert str(error.value) == "invalid id"

def test_fails_add_menu_when_menu_existed(override_get_uow, owner_ex, restaurant_ex, menu_ex):
    add_menu(override_get_uow, owner_ex, restaurant_ex, menu_ex)
    with pytest.raises(errors.DuplicatedException) as error:
        menu.add_menu(1, menu_ex, override_get_uow)
    assert str(error.value) == "existed data"

def test_success_get_menu_for_restaurant(override_get_uow, owner_ex, restaurant_ex, menu_ex):
    add_menu(override_get_uow, owner_ex, restaurant_ex, menu_ex)
    result = menu.get_menu_for_restaurant(1, override_get_uow)
    assert result == menu_ex

def test_fails_get_menu_for_restaurant_when_menu_not_existed(override_get_uow, owner_ex, restaurant_ex):
    add_restaurant(override_get_uow, owner_ex, restaurant_ex)
    with pytest.raises(errors.NotFoundException) as error:
        menu.get_menu_for_restaurant(1, override_get_uow)
    assert str(error.value) == "data not existed"

def test_success_update_menu(override_get_uow, owner_ex, restaurant_ex, menu_ex):
    add_menu(override_get_uow, owner_ex, restaurant_ex, menu_ex)
    menu_ex.menu["pasta"] = 8000
    result = menu.update_menu(1, menu_ex, override_get_uow)
    assert result == menu_ex

def test_fails_update_menu_when_restaurant_not_existed(override_get_uow, owner_ex, restaurant_ex, menu_ex):
    with pytest.raises(errors.NotFoundException) as error:
        menu.update_menu(1, menu_ex, override_get_uow)
    assert str(error.value) == "data not existed"

