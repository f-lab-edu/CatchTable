from app.allocation.domain import schemas, model
from app.allocation.service_layer import unit_of_work, errors


def add_owner(schema: schemas.Owner, uow: unit_of_work.AbstractUnitOfWork):
    if None in vars(schema).values():
        raise errors.InvalidDataException(f"invalid data")
    with uow:
        if uow.batches.is_owner_existed(schema.name, schema.phone):
            raise errors.DuplicatedException(f"existed data")

        owner = model.Owner(name=schema.name, phone=schema.phone, email=schema.email)
        uow.batches.add(owner)
        uow.commit()
        uow.batches.refresh(owner)
        result = schemas.Owner.from_orm(owner)
    return result


def get_owner(id: int, uow: unit_of_work.AbstractUnitOfWork):
    with uow:
        owner = uow.batches.get(model.Owner, id)
        result = schemas.Owner.from_orm(owner)
    return result


def get_owner_list(uow: unit_of_work.AbstractUnitOfWork):
    with uow:
        owners = uow.batches.list(model.Owner)
        results = [schemas.Owner.from_orm(o) for o in owners]
    return results


def delete_owner(id: int, uow: unit_of_work.AbstractUnitOfWork):
    with uow:
        owner = uow.batches.get(model.Owner, id)
        if not owner:
            return None     #test code 작성 후 Exception 처리 needed

        uow.batches.delete(owner)
        uow.commit()
    return owner