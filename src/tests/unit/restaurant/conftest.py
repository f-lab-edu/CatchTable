import pytest
from app.domain.schemas import Restaurant
from tests.unit.owner.conftest import *
from app.service_layer.services import owner, restaurant


@pytest.fixture
def restaurant_ex():
    return Restaurant(name="starbucks",
                      description="World Wide Coffe Shop",
                      phone="000-000-0000",
                      address="Seocho-Gu, Bangbae-Dong, 234",
                      city="seoul",
                      kind="cafe")

@pytest.fixture
def invalid_restaurant_ex():
    return Restaurant(name=None,
                      description="World Wide Coffe Shop",
                      phone="000-000-0000",
                      address="Seocho-Gu, Bangbae-Dong, 234",
                      city="seoul",
                      kind="cafe")

@pytest.fixture
def create_restaurant(create_owner, restaurant_ex, override_get_uow):
    restaurant.add_restaurant(1, restaurant_ex, override_get_uow)

@pytest.fixture
def create_owner(owner_ex, override_get_uow):
    owner.add_owner(owner_ex, override_get_uow)