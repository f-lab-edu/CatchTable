import pytest
import app.domain.model as model
from app.service_layer import errors
from app.service_layer.services import owner

def test_success_add_owner(override_get_uow, owner_ex):
    owner.add_owner(owner_ex, override_get_uow)
    assert override_get_uow.batches.get(model.Owner, 1) is not None

def test_fails_add_owner_when_owner_already_existed(override_get_uow, owner_ex):
    owner.add_owner(owner_ex, override_get_uow)
    with pytest.raises(errors.DuplicatedException) as error:
        owner.add_owner(owner_ex, override_get_uow)
    assert str(error.value) == "existed data"

def test_fails_add_owner_when_input_invalid_owner(override_get_uow, invalid_owner_ex):
    with pytest.raises(errors.InvalidDataException) as error:
        owner.add_owner(invalid_owner_ex, override_get_uow)
    assert str(error.value) == "invalid data"

def test_success_get_owner(override_get_uow, owner_ex):
    owner.add_owner(owner_ex, override_get_uow)
    result = owner.get_owner(1, override_get_uow)
    assert result == owner_ex

def test_fails_get_owner_when_owner_not_existed(override_get_uow):
    with pytest.raises(errors.NotFoundException) as error:
        owner.get_owner(1, override_get_uow)
    assert str(error.value) == "data not existed"

def test_success_get_owner_list(override_get_uow, owner_ex):
    owner.add_owner(owner_ex, override_get_uow)
    result = owner.get_owner_list(override_get_uow)
    assert result == [owner_ex]

def test_fails_get_owner_list_when_owner_data_not_existed(override_get_uow):
    with pytest.raises(errors.NotFoundException) as error:
        owner.get_owner_list(override_get_uow)
    assert str(error.value) == "data not existed"

def test_success_update_owner(override_get_uow, owner_ex):
    owner.add_owner(owner_ex, override_get_uow)
    owner_ex.email = "chulsu@google.com"
    result = owner.update_owner(1, owner_ex, override_get_uow)
    assert result == owner_ex

def test_fails_update_owner_when_owner_data_not_existed(override_get_uow, owner_ex):
    with pytest.raises(errors.NotFoundException) as error:
        owner.update_owner(1, owner_ex, override_get_uow)
    assert str(error.value) == "data not existed"

def test_success_delete_owner(override_get_uow, owner_ex):
    owner.add_owner(owner_ex, override_get_uow)
    owner.delete_owner(1, override_get_uow)
    assert override_get_uow.batches.get(model.Owner, 1) is None
