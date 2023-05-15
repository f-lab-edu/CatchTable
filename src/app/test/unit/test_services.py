from app.allocation.domain import schemas, model
from app.allocation.adapters import repository
from app.allocation.service_layer import unit_of_work, services
import pytest

class FakeRepository(repository.AbstractRepository):
    def __init__(self, batches_):
        self.batches_ = set(batches_)
        self.id = 0

    def add(self, batch):
        batch.id = self.id
        self.batches_.add(batch)
        self.id += 1

    def get(self, batch, id):
        for b in self.batches_:
            if (b.id == id):
                return b
        return None

    def get_menu(self, batch, restaurant_id):
        return next(b for b in self.batches_ if m.restaurant_id == restaurant_id)

    def list(self, batch, filter=None, value=None):
        if filter == 'name':
            return next(b for b in self.batches_ if b.name == value)
        elif filter == 'city':
            return next(b for b in self.batches_ if b.city == value)
        elif filter == 'kind':
            return next(b for b in self.batches_ if b.kind == value)

    def update(self, batch, updates):
        return batch

    def delete(self, batch):
        return batch

    def refresh(self, batch):
        return batch

    def is_owner_existed(self, batch, name, phone):
        for b in self.batches_:
            if type(b) == model.Owner:
                if (b.name == name) and (b.phone == phone):
                    return b
        return None

    def is_restaurant_existed(self, batch, owner_id, name, address):
        for b in self.batches_:
            if type(b) == model.Restaurant:
                if (b.owner_id == owner_id) and (b.name == name) and (b.address == address):
                    return b
        return None


class FakeUnitOfWork(unit_of_work.AbstractUnitOfWork):
    def __init__(self):
        self.batches = FakeRepository([])
        self.committed = False

    def commit(self):
        self.committed = True

    def rollback(self):
        pass


def common_owner_schema():
    return schemas.Owner(name="Hong Gil-Dong",
                         phone="000-111-1111",
                         email="Gil-Dong@gmail.com")

def common_restaurant_schema(owner_id):
    return schemas.Restaurant(name="starbucks",
                             owner_id=owner_id,
                             description="World Wide Coffe Shop",
                             phone="000-000-0000",
                             address="Seocho-Gu, Bangbae-Dong, 234",
                             city="seoul",
                             kind="cafe")

def test_add_restaurant():
    uow = FakeUnitOfWork()
    owner = common_owner_schema()
    services.add_owner(owner, uow)

    owner_id = 0
    restaurant = common_restaurant_schema(owner_id)
    result = services.add_restaurant(owner_id, restaurant, uow)
    assert result == restaurant

def test_error_for_invalid_owner_id():
    uow = FakeUnitOfWork()
    owner = common_owner_schema()
    services.add_owner(owner, uow)

    owner_id = 1
    restaurant = common_restaurant_schema(owner_id)
    with pytest.raises(services.NotFoundException, match='invalid id'):
        services.add_restaurant(owner_id, restaurant, uow)

def test_error_for_duplicate_data():
    uow = FakeUnitOfWork()
    owner = common_owner_schema()
    services.add_owner(owner, uow)

    owner_id = 0
    restaurant = common_restaurant_schema(owner_id)
    services.add_restaurant(owner_id, restaurant, uow)

    duplicated_restaurant = common_restaurant_schema(owner_id)
    with pytest.raises(services.DuplicatedException, match='existed data'):
        services.add_restaurant(owner_id, duplicated_restaurant, uow)


