import pytest
import app.domain.model as model
from app.service_layer import errors
from app.service_layer.services import owner, registration


def test_success_get_owner(override_get_uow, valid_owner_with_password, valid_owner):
    registration.add_user(valid_owner_with_password, override_get_uow)
    result = owner.get_owner(1, override_get_uow)
    assert result == valid_owner


def test_fails_get_owner_when_owner_not_existed(override_get_uow):
    with pytest.raises(errors.NotFoundException) as error:
        owner.get_owner(1, override_get_uow)



def test_success_get_owner_list(
    override_get_uow, valid_owner_with_password, valid_owner
):
    registration.add_user(valid_owner_with_password, override_get_uow)
    result = owner.get_owner_list(override_get_uow)
    assert result == [valid_owner]


def test_fails_get_owner_list_when_owner_data_not_existed(override_get_uow):
    with pytest.raises(errors.NotFoundException) as error:
        owner.get_owner_list(override_get_uow)



def test_success_update_owner(override_get_uow, valid_owner_with_password, valid_owner):
    registration.add_user(valid_owner_with_password, override_get_uow)
    valid_owner.email = "chulsu@google.com"
    result = owner.update_owner(1, valid_owner, override_get_uow)
    assert result == valid_owner


def test_fails_update_owner_when_owner_data_not_existed(override_get_uow, valid_owner):
    with pytest.raises(errors.NotFoundException) as error:
        owner.update_owner(1, valid_owner, override_get_uow)



def test_success_delete_owner(override_get_uow, valid_owner_with_password, valid_owner):
    registration.add_user(valid_owner_with_password, override_get_uow)
    owner.delete_owner(1, override_get_uow)
    assert override_get_uow.batches.get(model.Owner, 1) is None
