from app.allocation.domain import model, schema
from app.allocation.service_layer import unit_of_work



def add_owner(
        entity: schema.Owner,
        uow: unit_of_work.AbstractUnitOfWork):
    with uow:
        uow.batches.add(model.Owner(name=entity.name,
                                    phone=entity.phone,
                                    email=entity.email))
        uow.commit()


def add_restaurant(
        owner_id: int,
        entity: schema.Restaurant,
        uow: unit_of_work.AbstractUnitOfWork):
    with uow:
        uow.batches.add(model.Restaurant(name=entity.name,
                                         owner_id=owner_id,
                                         description=entity.description,
                                         phone=entity.phone,
                                         address=entity.address,
                                         city=entity.city,
                                         kind=entity.kind))
        uow.commit()


def add_menu(
        restaurant_id: int,
        entity: schema.Menu,
        uow: unit_of_work.AbstractUnitOfWork):
    with uow:
        uow.batches.add(model.Menu(menu=entity.menu, restaurant_id=restaurant_id))
        uow.commit()


def get_restaurant(filter: str,
                   value: str,
                   uow: unit_of_work.AbstractUnitOfWork):
    if filter not in ['name', 'city', 'kind']:
        return None
    with uow:
        restaurants = uow.batches.get(model.Restaurant, filter, value)
        results = [schema.Restaurant.from_orm(r) for r in restaurants]
    return results


