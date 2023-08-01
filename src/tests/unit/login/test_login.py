import pytest
from app.domain import model
from app.service_layer import errors
from app.service_layer.services import login



def test_success_authenticate_user(override_get_uow, valid_owner_with_password):
    login.add_user(valid_owner_with_password, override_get_uow)
    result = login.authenticate_user(valid_owner_with_password.email, valid_owner_with_password.hashed_password, override_get_uow)
    assert result == True

def test_fail_authenticate_user_when_password_not_matched(override_get_uow, valid_owner_with_password):
    login.add_user(valid_owner_with_password, override_get_uow)
    result = login.authenticate_user(valid_owner_with_password.email, "2222", override_get_uow)
    assert result == False

def test_fail_check_user_existed_when_data_not_existed(override_get_uow, valid_owner_with_password):
    with pytest.raises(errors.NotFoundException) as error:
        login.check_user_existed(model.Owner, valid_owner_with_password.email, override_get_uow)
    assert str(error.value) == "data not existed"
