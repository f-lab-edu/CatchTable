from app.allocation.domain import schemas, model
from app.allocation.service_layer import unit_of_work, errors


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


def get_menu_for_restaurant(restaurant_id: int, uow: unit_of_work.AbstractUnitOfWork):
    with uow:
        menu = uow.batches.get_menu(restaurant_id)
        if not menu:
            raise errors.NotFoundException(f"data not existed")
        result = schemas.Menu.from_orm(menu)
    return result


def update_menu(restaurant_id: int, schema: schemas.Menu, uow: unit_of_work.AbstractUnitOfWork):
    with uow:
        menu = uow.batches.get_menu(restaurant_id)
        if not menu:
            raise errors.NotFoundException(f"data not existed")
        updates = schema.dict(exclude_unset=True)
        result = schemas.Menu.from_orm(uow.batches.update(menu, updates))
        uow.commit()
    return result