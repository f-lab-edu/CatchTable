from app.allocation.domain import schemas, model
from app.allocation.service_layer import unit_of_work
from typing import Union


## POST
def add_owner(schema: schemas.Owner, uow: unit_of_work.AbstractUnitOfWork):
    with uow:
        owner = model.Owner(name=schema.name, phone=schema.phone, email=schema.email)
        uow.batches.add(owner)
        uow.commit()
        uow.batches.refresh(owner)
        result = schemas.Owner.from_orm(owner)
    return result


def add_restaurant(owner_id: int, schema: schemas.Restaurant, uow: unit_of_work.AbstractUnitOfWork):
    with uow:
        restaurant = model.Restaurant(name=schema.name,
                                         owner_id=owner_id,
                                         description=schema.description,
                                         phone=schema.phone,
                                         address=schema.address,
                                         city=schema.city,
                                         kind=schema.kind)
        uow.batches.add(restaurant)
        uow.commit()
        uow.batches.refresh(restaurant)
        result = schemas.Restaurant.from_orm(restaurant)
    return result


def add_menu(restaurant_id: int, schema: schemas.Menu, uow: unit_of_work.AbstractUnitOfWork):
    with uow:
        menu = model.Menu(menu=schema.menu, id=restaurant_id)
        uow.batches.add(menu)
        uow.commit()
        uow.batches.refresh(menu)
        result = schemas.Menu.from_orm(menu)
    return result


## GET
def get_restaurant(id: int, uow: unit_of_work.AbstractUnitOfWork):
    with uow:
        restaurant = uow.batches.get(model.Restaurant, id)
        result = schemas.Restaurant.from_orm(restaurant)
    return result


def get_menu_for_restaurant(id: int, uow: unit_of_work.AbstractUnitOfWork):
    with uow:
        menu = uow.batches.get(model.Menu, id)
        result = schemas.Menu.from_orm(menu)
    return result


def get_restaurant_list(filter: str, value: Union[str, int], uow: unit_of_work.AbstractUnitOfWork):
    if filter not in ['name', 'city', 'kind']:
        return None
    with uow:
        restaurants = uow.batches.list(model.Restaurant, filter=filter, value=value)
        results = [schemas.Restaurant.from_orm(r) for r in restaurants]
    return results


## PUT
def update_restaurant(id: int, schema: schemas.Restaurant, uow: unit_of_work.AbstractUnitOfWork):
    with uow:
        restaurant = uow.batches.get(model.Restaurant, id)
        if not restaurant:
            return None

        updates = schema.dict(exclude_unset=True)
        restaurant = uow.batches.update(restaurant, updates)
        result = schemas.Restaurant.from_orm(restaurant)
        uow.commit()
    return result


def update_menu(id: int, schema: schemas.Menu, uow: unit_of_work.AbstractUnitOfWork):
    with uow:
        menu = uow.batches.get(model.Menu, id)
        if not menu:
            return None

        updates = schema.dict(exclude_unset=True)
        result = schemas.Menu.from_orm(uow.batches.update(menu, updates))
        uow.commit()
    return result


## DELETE
def delete_restaurant(id: int, uow: unit_of_work.AbstractUnitOfWork):
    with uow:
        menu = uow.batches.get(model.Menu, id)
        if not menu:
            return None

        restaurant = uow.batches.get(model.Restaurant, id)
        if not restaurant:
            return None

        uow.batches.delete(menu)
        uow.batches.delete(restaurant)
        uow.commit()
    return restaurant