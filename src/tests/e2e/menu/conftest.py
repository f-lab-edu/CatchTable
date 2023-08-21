import pytest
import json
from tests.unit.menu.conftest import *

@pytest.fixture
def valid_menu_json(valid_menu):
    return json.loads(valid_menu.json())



