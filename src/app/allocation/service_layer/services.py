from app.allocation.domain import schemas, model
from app.allocation.service_layer import unit_of_work, errors
from typing import Union


def add_owner(schema: schemas.Owner, uow: unit_of_work.AbstractUnitOfWork):
    with uow:
        if uow.batches.is_owner_existed(schema.name, schema.phone):
            raise errors.DuplicatedException(f"existed data")

        owner = model.Owner(name=schema.name, phone=schema.phone, email=schema.email)
        uow.batches.add(owner)
        uow.commit()
        uow.batches.refresh(owner)
        result = schemas.Owner.from_orm(owner)
    return result


def add_restaurant(owner_id: int, schema: schemas.Restaurant, uow: unit_of_work.AbstractUnitOfWork):
    with uow:
        if not uow.batches.get(model.Owner, owner_id):
            raise errors.NotFoundException(f"invalid id")

        if uow.batches.is_restaurant_existed(owner_id, schema.name, schema.address):
            raise errors.DuplicatedException(f"existed data")

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
        if not uow.batches.get(model.Restaurant, restaurant_id):
            raise errors.NotFoundException(f"invalid id")

        if uow.batches.get_menu(restaurant_id):
            raise errors.DuplicatedException(f"existed data")

        menu = model.Menu(menu=schema.menu, restaurant_id=restaurant_id)
        uow.batches.add(menu)
        uow.commit()
        uow.batches.refresh(menu)
        result = schemas.Menu.from_orm(menu)
    return result


# restaurant이 존재하지 않는데도 계속 get을 해오고 있어!!!!!!!!
def get_restaurant(id: int, uow: unit_of_work.AbstractUnitOfWork):
    with uow:
        restaurant = uow.batches.get(model.Restaurant, id)
        result = schemas.Restaurant.from_orm(restaurant)
    return result


def get_menu_for_restaurant(restaurant_id: int, uow: unit_of_work.AbstractUnitOfWork):
    with uow:
        menu = uow.batches.get_menu(restaurant_id)
        result = schemas.Menu.from_orm(menu)
    return result


def get_restaurant_list(filter: str, value: Union[str, int], uow: unit_of_work.AbstractUnitOfWork):
    if filter not in ['name', 'city', 'kind']:
        return None # raise로 고칠 것
    with uow:
        restaurants = uow.batches.list(model.Restaurant, filter=filter, value=value)
        results = [schemas.Restaurant.from_orm(r) for r in restaurants]
    return results


def update_restaurant(id: int, schema: schemas.Restaurant, uow: unit_of_work.AbstractUnitOfWork):
    with uow:
        restaurant = uow.batches.get(model.Restaurant, id)
        if not restaurant:
            return None # raise로 고칠 것

        updates = schema.dict(exclude_unset=True)
        restaurant = uow.batches.update(restaurant, updates)
        result = schemas.Restaurant.from_orm(restaurant)
        uow.commit()
    return result


def update_menu(restaurant_id: int, schema: schemas.Menu, uow: unit_of_work.AbstractUnitOfWork):
    with uow:
        menu = uow.batches.get_menu(restaurant_id)
        if not menu:
            return None  # raise로 고칠 것

        updates = schema.dict(exclude_unset=True)
        result = schemas.Menu.from_orm(uow.batches.update(menu, updates))
        uow.commit()
    return result


def delete_restaurant(id: int, uow: unit_of_work.AbstractUnitOfWork):
    with uow:
        restaurant = uow.batches.get(model.Restaurant, id)
        if not restaurant:
            return None # raise로

        uow.batches.delete(restaurant)
        uow.commit()
    return restaurant


def delete_owner(id: int, uow: unit_of_work.AbstractUnitOfWork):
    with uow:
        owner = uow.batches.get(model.Owner, id)
        if not owner:
            return None # raise로

        uow.batches.delete(owner)
        uow.commit()
    return owner