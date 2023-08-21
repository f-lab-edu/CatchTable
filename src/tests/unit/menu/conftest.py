import pytest
from app.domain.schemas import Menu


@pytest.fixture
def valid_menu():
    return Menu(menu={"steak": 30000, "pasta": 18000, "coke": 4000})
