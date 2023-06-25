import pytest
import src.app.domain.model as model
from src.app.service_layer import errors
from src.app.service_layer.services import restaurant

def test_add_restaurant(override_get_uow, create_owner, restaurant_ex):
    restaurant.add_restaurant(1, restaurant_ex, override_get_uow)
    assert override_get_uow.batches.get(model.Restaurant, 1) is not None

def test_add_restaurant_returns_error_when_input_invalid_data(override_get_uow, create_owner, invalid_restaurant_ex):
    with pytest.raises(errors.InvalidDataException) as error:
        restaurant.add_restaurant(1, invalid_restaurant_ex, override_get_uow)
    assert str(error.value) == "invalid data"

def test_add_restaurant_returns_error_when_invalid_owner_id(override_get_uow, create_owner, restaurant_ex):
    with pytest.raises(errors.NotFoundException) as error:
        restaurant.add_restaurant(2, restaurant_ex, override_get_uow)
    assert str(error.value) == "invalid id"

def test_add_restaurant_returns_error_when_data_already_existed(override_get_uow, create_owner, restaurant_ex):
    restaurant.add_restaurant(1, restaurant_ex, override_get_uow)
    with pytest.raises(errors.DuplicatedException) as error:
        restaurant.add_restaurant(1, restaurant_ex, override_get_uow)
    assert str(error.value) == "existed data"


def test_get_restaurant(override_get_uow, create_owner, create_restaurant, restaurant_ex):
    result = restaurant.get_restaurant(1, override_get_uow)
    assert result == restaurant_ex

def test_get_restaurant_returns_errors_when_restaurant_not_existed(override_get_uow):
    with pytest.raises(errors.NotFoundException) as error:
        restaurant.get_restaurant(1, override_get_uow)
    assert str(error.value) == "data not existed"

def test_get_restaurant_list(override_get_uow, create_restaurant, restaurant_ex):
    result = restaurant.get_restaurant_list("city", "seoul", override_get_uow)
    assert result == [restaurant_ex]

def test_get_restaurant_list_returns_error_input_invalid_filter(override_get_uow, create_restaurant):
    with pytest.raises(errors.NotFoundException) as error:
        restaurant.get_restaurant_list("something", "something", override_get_uow)
    assert str(error.value) == "filter not existed"

def test_update_restaurant(override_get_uow, create_restaurant, restaurant_ex):
    restaurant_ex.name = "blarblar cafe"
    result = restaurant.update_restaurant(1, restaurant_ex, override_get_uow)
    assert result == restaurant_ex

def test_update_restaurant_returns_error_when_data_not_existed(override_get_uow):
    with pytest.raises(errors.NotFoundException) as error:
        restaurant.get_restaurant_list("city", "seoul", override_get_uow)
    assert str(error.value) == "data not existed"

def test_delete_restaurant(override_get_uow, create_restaurant):
    restaurant.delete_restaurant(1, override_get_uow)
    assert override_get_uow.batches.get(model.Restaurant, 1) is None