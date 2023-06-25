import pytest
import src.app.domain.model as model
from src.app.service_layer import errors
from src.app.service_layer.services import menu


def test_add_menu(override_get_uow, create_restaurant, menu_ex):
    menu.add_menu(1, menu_ex, override_get_uow)
    assert override_get_uow.batches.get(model.Menu, 1) is not None

def test_add_menu_returns_error_when_restaurant_not_found(override_get_uow, menu_ex):
    with pytest.raises(errors.NotFoundException) as error:
        menu.add_menu(1, menu_ex, override_get_uow)
    assert str(error.value) == "invalid id"

def test_add_menu_returns_error_when_menu_existed(override_get_uow, create_menu, menu_ex):
    with pytest.raises(errors.DuplicatedException) as error:
        menu.add_menu(1, menu_ex, override_get_uow)
    assert str(error.value) == "existed data"

def test_get_menu_for_restaurant(override_get_uow, create_menu, menu_ex):
    result = menu.get_menu_for_restaurant(1, override_get_uow)
    assert result == menu_ex

def test_get_menu_for_restaurant_returns_error_when_menu_not_existed(override_get_uow, create_restaurant):
    with pytest.raises(errors.NotFoundException) as error:
        menu.get_menu_for_restaurant(1, override_get_uow)
    assert str(error.value) == "data not existed"

def test_update_menu(override_get_uow, create_menu, menu_ex):
    menu_ex.menu["pasta"] = 8000
    result = menu.update_menu(1, menu_ex, override_get_uow)
    assert result == menu_ex

def test_update_menu_returns_error_when_restaurant_not_existed(override_get_uow, menu_ex):
    with pytest.raises(errors.NotFoundException) as error:
        menu.update_menu(1, menu_ex, override_get_uow)
    assert str(error.value) == "data not existed"

