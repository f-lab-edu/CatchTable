import pytest
import app.domain.model as model
from app.service_layer import errors
from app.service_layer.services import registration, restaurant, menu
from tests.unit.restaurant.test_restaurant_services import add_restaurant


def add_menu(override_get_uow, valid_owner_with_password, valid_restaurant, valid_menu):
    registration.add_user(valid_owner_with_password, override_get_uow)
    restaurant.add_restaurant(1, valid_restaurant, override_get_uow)
    menu.add_menu(1, valid_menu, override_get_uow)


def test_success_add_menu(
    override_get_uow, valid_owner_with_password, valid_restaurant, valid_menu
):
    add_menu(override_get_uow, valid_owner_with_password, valid_restaurant, valid_menu)
    assert override_get_uow.batches.get(model.Menu, 1) is not None


def test_fails_add_menu_when_restaurant_not_found(override_get_uow, valid_menu):
    with pytest.raises(errors.NotFoundException) as error:
        menu.add_menu(1, valid_menu, override_get_uow)
    assert str(error.value) == "invalid id"


def test_fails_add_menu_when_menu_existed(
    override_get_uow, valid_owner_with_password, valid_restaurant, valid_menu
):
    add_menu(override_get_uow, valid_owner_with_password, valid_restaurant, valid_menu)
    with pytest.raises(errors.DuplicatedException) as error:
        menu.add_menu(1, valid_menu, override_get_uow)
    assert str(error.value) == "existed data"


def test_success_get_menu_for_restaurant(
    override_get_uow, valid_owner_with_password, valid_restaurant, valid_menu
):
    add_menu(override_get_uow, valid_owner_with_password, valid_restaurant, valid_menu)
    result = menu.get_menu_for_restaurant(1, override_get_uow)
    assert result == valid_menu


def test_fails_get_menu_for_restaurant_when_menu_not_existed(
    override_get_uow, valid_owner_with_password, valid_restaurant
):
    add_restaurant(override_get_uow, valid_owner_with_password, valid_restaurant)
    with pytest.raises(errors.NotFoundException) as error:
        menu.get_menu_for_restaurant(1, override_get_uow)
    assert str(error.value) == "data not existed"


def test_success_update_menu(
    override_get_uow, valid_owner_with_password, valid_restaurant, valid_menu
):
    add_menu(override_get_uow, valid_owner_with_password, valid_restaurant, valid_menu)
    valid_menu.menu["pasta"] = 8000
    result = menu.update_menu(1, valid_menu, override_get_uow)
    assert result == valid_menu


def test_fails_update_menu_when_restaurant_not_existed(override_get_uow, valid_menu):
    with pytest.raises(errors.NotFoundException) as error:
        menu.update_menu(1, valid_menu, override_get_uow)
    assert str(error.value) == "data not existed"
