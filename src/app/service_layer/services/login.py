from app.domain import schemas, model
from app.service_layer import unit_of_work, errors, utils




def add_user(schema: schemas.OwnerCreate, uow: unit_of_work.AbstractUnitOfWork) -> schemas.Owner:
    with uow:
        if uow.batches.is_user_existed(model.Owner, schema.email):
            raise errors.DuplicatedException("existed data")

        user_model = create_user_owner(schema)
        uow.batches.add(user_model)
        uow.commit()
        user_schema = schemas.Owner.from_orm(user_model)
    return user_schema

def create_user_owner(schema: schemas.OwnerCreate) -> model.Owner:
    hashed_password = utils.get_password_hash(schema.hashed_password)
    return model.Owner(username=schema.username, name=schema.name, phone=schema.phone,
                       email=schema.email, hashed_password=hashed_password)




def authenticate_user(email: str, password: str, uow:unit_of_work.AbstractUnitOfWork) -> bool:
    user = check_user_existed(model.Owner, email, uow)
    return utils.verify_password(password, user.hashed_password)

def check_user_existed(model: type(model.Owner), email: str, uow: unit_of_work.AbstractUnitOfWork) -> schemas.OwnerCreate:
    with uow:
        user_model = uow.batches.get_user(model, email)
        if not user_model:
            raise errors.NotFoundException("data not existed")
        user_schema = schemas.OwnerCreate.from_orm(user_model)
    return user_schema







