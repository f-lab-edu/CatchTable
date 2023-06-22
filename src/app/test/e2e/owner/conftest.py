import pytest

@pytest.fixture
def owner_id():
    return 1

@pytest.fixture
def owner_ex():
    return {
            "name":"Hong Gil-Dong",
            "phone":"000-111-1111",
            "email":"Gil-Dong@gmail.com"
            }

@pytest.fixture
def invalid_type_of_owner_ex():
    return {
            "names":"Hong Gil-Dong",
            "phones":"000-111-1111",
            "test":"Gil-Dong@gmail.com"
            }