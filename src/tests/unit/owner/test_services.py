import pytest
import app.domain.model as model
from app.service_layer import errors
from app.service_layer.services import owner

def test_add_owner(override_get_uow, owner_ex):
    owner.add_owner(owner_ex, override_get_uow)
    assert override_get_uow.batches.get(model.Owner, 1) is not None

def test_add_owner_returns_error_when_owner_already_existed(override_get_uow, owner_ex):
    owner.add_owner(owner_ex, override_get_uow)
    with pytest.raises(errors.DuplicatedException) as error:
        owner.add_owner(owner_ex, override_get_uow)
    assert str(error.value) == "existed data"

def test_add_owner_returns_error_when_input_invalid_owner(override_get_uow, invalid_owner_ex):
    with pytest.raises(errors.InvalidDataException) as error:
        owner.add_owner(invalid_owner_ex, override_get_uow)
    assert str(error.value) == "invalid data"

def test_get_owner(override_get_uow, owner_ex):
    owner.add_owner(owner_ex, override_get_uow)
    result = owner.get_owner(1, override_get_uow)
    assert result == owner_ex