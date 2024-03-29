from app.domain import schemas, model
from app.service_layer import unit_of_work, errors


def get_owner(id: int, uow: unit_of_work.AbstractUnitOfWork):
    with uow:
        owner = uow.batches.get(model.Owner, id)
        result = schemas.Owner.from_orm(owner)
        if not all(result.dict().values()):
            raise errors.NotFoundException("data not existed")
    return result


def get_owner_list(uow: unit_of_work.AbstractUnitOfWork):
    with uow:
        owners = uow.batches.list(model.Owner)
        results = [schemas.Owner.from_orm(o) for o in owners]
        if not results:
            raise errors.NotFoundException("data not existed")
    return results


def update_owner(id: int, schema: schemas.Owner, uow: unit_of_work.AbstractUnitOfWork):
    with uow:
        owner = uow.batches.get(model.Owner, id)
        if not owner:
            raise errors.NotFoundException("data not existed")

        updates = schema.dict(exclude_unset=True)
        owner = uow.batches.update(owner, updates)
        result = schemas.Owner.from_orm(owner)
        uow.commit()
    return result


def delete_owner(id: int, uow: unit_of_work.AbstractUnitOfWork):
    with uow:
        owner = uow.batches.get(model.Owner, id)
        if not owner:
            raise errors.NotFoundException("data not existed")
        uow.batches.delete(owner)
        uow.commit()
    return owner
