from fastapi import APIRouter, HTTPException, Depends
from app.domain import schemas
from app.entrypoints.dependencies import get_uow
from app.service_layer import unit_of_work, errors
from app.service_layer.services import login
from typing_extensions import Annotated


router = APIRouter()


@router.post("/login/", status_code=200)
async def user_login(
    user: schemas.OwnerCreate,
    uow: Annotated[unit_of_work.AbstractUnitOfWork, Depends(get_uow)],
):
    try:
        return login.authenticate_user(user.email, user.hashed_password, uow)
    except errors.NotFoundException:
        raise HTTPException(status_code=404, detail="email not existed")
    except errors.PasswordNotMatchedException:
        raise HTTPException(status_code=404, detail="password not matched")
