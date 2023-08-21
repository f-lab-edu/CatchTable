import pytest
import json
from tests.unit.restaurant.conftest import *

@pytest.fixture
def valid_restaurant_json(valid_restaurant):
    return json.loads(valid_restaurant.json())

@pytest.fixture
def invalid_restaurant_json(invalid_restaurant):
    return json.loads(invalid_restaurant.json())

