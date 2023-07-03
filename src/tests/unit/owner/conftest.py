import pytest
from app.domain.schemas import Owner


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

