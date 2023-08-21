from app.domain import schemas, model
from app.service_layer import unit_of_work, errors, utils


def add_user(
    schema: schemas.OwnerCreate, uow: unit_of_work.AbstractUnitOfWork
) -> schemas.Owner:
    with uow:
        if uow.batches.is_user_existed(model.Owner, schema.email):
            raise errors.DuplicatedException("existed data")

        user_model = get_owner_schema_with_password(schema)
        uow.batches.add(user_model)
        uow.commit()
        user_schema = schemas.Owner.from_orm(user_model)
    return user_schema


def get_owner_schema_with_password(schema: schemas.OwnerCreate) -> model.Owner:
    hashed_password = utils.get_password_hash(schema.hashed_password)
    return model.Owner(
        name=schema.name,
        phone=schema.phone,
        email=schema.email,
        hashed_password=hashed_password,
    )
