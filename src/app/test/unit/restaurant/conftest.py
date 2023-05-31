import pytest
from app.test.unit.owner import conftest

@pytest.fixture
def restaurant_id():
    return 1

@pytest.fixture
def restaurant_ex():
    return { "name": "starbucks",
             "description": "World Wide Coffe Shop",
             "phone": "000-000-0000",
             "address": "Seocho-Gu, Bangbae-Dong, 234",
             "city" : "seoul",
             "kind": "cafe"
            }

@pytest.fixture
def invalid_type_of_restaurant_ex():
    return { "test": "starbucks",
             "test3": "World Wide Coffe Shop",
             "phone": "000-000-0000",
             "address": "Seocho-Gu, Bangbae-Dong, 234",
             "city" : "seoul",
             "kind": "cafe"
            }
