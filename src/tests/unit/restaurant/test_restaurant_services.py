import pytest
import app.domain.model as model
from app.service_layer import errors
from app.service_layer.services import owner, restaurant

def add_restaurant(override_get_uow, owner_ex, restaurant_ex):
    owner.add_owner(owner_ex, override_get_uow)
    restaurant.add_restaurant(1, restaurant_ex, override_get_uow)

def test_success_add_restaurant(override_get_uow, owner_ex, restaurant_ex):
    add_restaurant(override_get_uow, owner_ex, restaurant_ex)
    assert override_get_uow.batches.get(model.Restaurant, 1) is not None

def test_fails_add_restaurant_when_input_invalid_data(override_get_uow, owner_ex, invalid_restaurant_ex):
    owner.add_owner(owner_ex, override_get_uow)
    with pytest.raises(errors.InvalidDataException) as error:
        restaurant.add_restaurant(1, invalid_restaurant_ex, override_get_uow)
    assert str(error.value) == "invalid data"

def test_fails_add_restaurant_when_invalid_owner_id(override_get_uow, owner_ex, restaurant_ex):
    owner.add_owner(owner_ex, override_get_uow)
    with pytest.raises(errors.NotFoundException) as error:
        restaurant.add_restaurant(2, restaurant_ex, override_get_uow)
    assert str(error.value) == "invalid id"

def test_fails_add_restaurant_when_data_already_existed(override_get_uow, owner_ex, restaurant_ex):
    add_restaurant(override_get_uow, owner_ex, restaurant_ex)
    with pytest.raises(errors.DuplicatedException) as error:
        restaurant.add_restaurant(1, restaurant_ex, override_get_uow)
    assert str(error.value) == "existed data"

def test_success_get_restaurant(override_get_uow, owner_ex, restaurant_ex):
    owner.add_owner(owner_ex, override_get_uow)
    restaurant.add_restaurant(1, restaurant_ex, override_get_uow)
    result = restaurant.get_restaurant(1, override_get_uow)
    assert result == restaurant_ex

def test_fails_get_restaurant_when_restaurant_not_existed(override_get_uow, owner_ex, restaurant_ex):
    with pytest.raises(errors.NotFoundException) as error:
        restaurant.get_restaurant(1, override_get_uow)
    assert str(error.value) == "data not existed"

def test_success_get_restaurant_list(override_get_uow, owner_ex, restaurant_ex):
    add_restaurant(override_get_uow, owner_ex, restaurant_ex)
    result = restaurant.get_restaurant_list("city", "seoul", override_get_uow)
    assert result == [restaurant_ex]

def test_fails_get_restaurant_list_when_input_invalid_filter(override_get_uow, owner_ex, restaurant_ex):
    add_restaurant(override_get_uow, owner_ex, restaurant_ex)
    with pytest.raises(errors.NotFoundException) as error:
        restaurant.get_restaurant_list("something", "something", override_get_uow)
    assert str(error.value) == "filter not existed"

def test_success_update_restaurant(override_get_uow, owner_ex, restaurant_ex):
    add_restaurant(override_get_uow, owner_ex, restaurant_ex)
    restaurant_ex.name = "blarblar cafe"
    result = restaurant.update_restaurant(1, restaurant_ex, override_get_uow)
    assert result == restaurant_ex

def test_fails_update_restaurant_when_data_not_existed(override_get_uow):
    with pytest.raises(errors.NotFoundException) as error:
        restaurant.get_restaurant_list("city", "seoul", override_get_uow)
    assert str(error.value) == "data not existed"

def test_success_delete_restaurant(override_get_uow, owner_ex, restaurant_ex):
    add_restaurant(override_get_uow, owner_ex, restaurant_ex)
    restaurant.delete_restaurant(1, override_get_uow)
    assert override_get_uow.batches.get(model.Restaurant, 1) is None