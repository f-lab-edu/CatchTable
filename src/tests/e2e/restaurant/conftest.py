import pytest
import json
from tests.unit.restaurant.conftest import *

@pytest.fixture
def restaurant_ex_json(restaurant_ex):
    return json.loads(restaurant_ex.json())

@pytest.fixture
def invalid_restaurant_ex_json(invalid_restaurant_ex):
    return json.loads(invalid_restaurant_ex.json())

