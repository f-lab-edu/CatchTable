from app.allocation.domain import model, schemas
from app.allocation.service_layer import unit_of_work
from typing import Union



def add_owner(
        schema: schemas.Owner,
        uow: unit_of_work.AbstractUnitOfWork):
    with uow:
        uow.batches.add(model.Owner(name=schema.name,
                                    phone=schema.phone,
                                    email=schema.email))
        uow.commit()


def add_restaurant(
        owner_id: int,
        schema: schemas.Restaurant,
        uow: unit_of_work.AbstractUnitOfWork):
    with uow:
        uow.batches.add(model.Restaurant(name=schema.name,
                                         owner_id=owner_id,
                                         description=schema.description,
                                         phone=schema.phone,
                                         address=schema.address,
                                         city=schema.city,
                                         kind=schema.kind))
        uow.commit()


def add_menu(
        restaurant_id: int,
        schema: schemas.Menu,
        uow: unit_of_work.AbstractUnitOfWork):
    with uow:
        uow.batches.add(model.Menu(menu=schema.menu, restaurant_id=restaurant_id))
        uow.commit()


def get_restaurants(filter: str,
                   value: Union[str, int],
                   uow: unit_of_work.AbstractUnitOfWork):
    #
    if filter not in ['id', 'name', 'city', 'kind']:
        return None
    with uow:
        restaurants = uow.batches.get(model.Restaurant, filter, value)
        results = [schemas.Restaurant.from_orm(r) for r in restaurants]
    return results


def update_restaurant(restaurant_id: int,
                      schema: schemas.Restaurant,
                      uow: unit_of_work.AbstractUnitOfWork):
    with uow:
        updates = schema.dict(exclude_unset=True)
        restaurant = uow.batches.update(model.Restaurant,
                                         'id',
                                         restaurant_id,
                                         updates)
        result = schemas.Restaurant.from_orm(restaurant)
        uow.commit()
    return result


def delete_restaurant(restaurant_id: int, uow: unit_of_work.AbstractUnitOfWork):
    with uow:
        uow.batches.delete(model.Menu,
                           'restaurant_id',
                           restaurant_id)
        uow.batches.delete(model.Restaurant,
                           'id',
                           restaurant_id)
        uow.commit()