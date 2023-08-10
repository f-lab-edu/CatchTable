from app.domain import schemas, model
from app.service_layer import unit_of_work, errors, utils


def authenticate_user(
    email: str, password: str, uow: unit_of_work.AbstractUnitOfWork
) -> bool:
    user = check_user_existed(model.Owner, email, uow)
    return check_password_matched(password, user.hashed_password)


def check_user_existed(
    model: type(model.Owner), email: str, uow: unit_of_work.AbstractUnitOfWork
) -> schemas.OwnerCreate:
    with uow:
        user_model = uow.batches.get_user(model, email)
        if not user_model:
            raise errors.NotFoundException("data not existed")
        user_schema = schemas.OwnerCreate.from_orm(user_model)
    return user_schema


def check_password_matched(
    password: str, hashed_password: str
) -> bool:
    try:
        matched = utils.verify_password(password, hashed_password)
        if not matched:
            raise errors.PasswordNotMatchedException("password not matched")
        return matched
    except errors.PasswordNotMatchedException:
        raise

