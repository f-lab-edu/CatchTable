import pytest
import json
from tests.unit.menu.conftest import *

@pytest.fixture
def menu_ex_json(menu_ex):
    return json.loads(menu_ex.json())

@pytest.fixture
def invalid_menu_ex_json(invalid_menu_ex):
    return json.loads(invalid_menu_ex.json())

