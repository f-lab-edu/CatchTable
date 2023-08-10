import pytest
from app.service_layer.services import registration
from app.service_layer import errors


def test_success_add_user(valid_owner_with_password, valid_owner, override_get_uow):
    result = registration.add_user(valid_owner_with_password, override_get_uow)
    assert result == valid_owner


def test_fails_add_user_when_user_email_already_existed(valid_owner_with_password, override_get_uow):
    registration.add_user(valid_owner_with_password, override_get_uow)
    with pytest.raises(errors.DuplicatedException) as error:
        registration.add_user(
            valid_owner_with_password, override_get_uow
        )
    assert str(error.value) == "existed data"
