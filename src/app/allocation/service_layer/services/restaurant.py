from app.allocation.domain import schemas, model
from app.allocation.service_layer import unit_of_work, errors
from typing import Union


def add_restaurant(owner_id: int, schema: schemas.Restaurant, uow: unit_of_work.AbstractUnitOfWork):
    if None in vars(schema).values():
        raise errors.InvalidDataException(f"invalid data")
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


def get_restaurant(id: int, uow: unit_of_work.AbstractUnitOfWork):
    with uow:
        restaurant = uow.batches.get(model.Restaurant, id)
        result = schemas.Restaurant.from_orm(restaurant)
        if not all(result.dict().values()):
            raise errors.NotFoundException(f"data not existed")
    return result


def get_restaurant_list(filter: str, value: Union[str, int], uow: unit_of_work.AbstractUnitOfWork):
    if filter not in ['name', 'city', 'kind']:
        raise errors.NotFoundException(f"filter not existed")
    with uow:
        restaurants = uow.batches.list_restaurants(model.Restaurant, filter=filter, value=value)
        results = [schemas.Restaurant.from_orm(r) for r in restaurants]
        if not results:
            raise errors.NotFoundException(f"data not existed")
    return results


def update_restaurant(id: int, schema: schemas.Restaurant, uow: unit_of_work.AbstractUnitOfWork):
    with uow:
        restaurant = uow.batches.get(model.Restaurant, id)
        if not restaurant:
            raise errors.NotFoundException(f"data not existed")

        updates = schema.dict(exclude_unset=True)
        restaurant = uow.batches.update(restaurant, updates)
        result = schemas.Restaurant.from_orm(restaurant)
        uow.commit()
    return result


def delete_restaurant(id: int, uow: unit_of_work.AbstractUnitOfWork):
    with uow:
        restaurant = uow.batches.get(model.Restaurant, id)
        if not restaurant:
            raise errors.NotFoundException(f"data not existed")

        uow.batches.delete(restaurant)
        uow.commit()
    return restaurant