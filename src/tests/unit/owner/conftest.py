import pytest
from app.domain.schemas import Owner
from app.service_layer.services import owner


@pytest.fixture
def owner_ex():
    return Owner(name="kim chul su",
                 phone="010-000-0000",
                 email="chulsu@mail.com")

@pytest.fixture
def invalid_owner_ex():
    return Owner(name=None,
                 phone="010-000-0000",
                 email="chulsu@mail.com")

@pytest.fixture
def create_owner(override_get_uow, owner_ex):
    owner.add_owner(owner_ex, override_get_uow)