import pytest
import json
from tests.unit.owner.conftest import *

@pytest.fixture
def valid_owner_with_password_json(valid_owner_with_password):
    return json.loads(valid_owner_with_password.json())

@pytest.fixture
def valid_owner_json(valid_owner):
    return json.loads(valid_owner.json())

