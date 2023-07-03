import pytest
from app.domain.schemas import Restaurant


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


