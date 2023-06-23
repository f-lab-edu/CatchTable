import pytest


@pytest.fixture
def menu_ex():
    return { "menu":
                    {
                    'steak': 30000,
                    'pasta': 18000,
                    'coke': 4000
                    }
            }