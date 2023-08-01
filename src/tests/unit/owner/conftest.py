import pytest
from app.domain.schemas import OwnerCreate, Owner

@pytest.fixture
def valid_owner_with_password():
    return OwnerCreate(
        username="chulsu12",
        hashed_password="1111",
        name="kim chul su",
        phone="010-000-0000",
        email="chulsu@mail.com"
    )

@pytest.fixture
def valid_owner():
    return Owner(
        username="chulsu12",
        name="kim chul su",
        phone="010-000-0000",
        email="chulsu@mail.com"
    )



