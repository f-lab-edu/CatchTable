from fastapi import APIRouter, HTTPException, Depends
from app.domain import schemas
from app.entrypoints.dependencies import get_uow
from app.service_layer import unit_of_work, errors
from app.service_layer.services import login as services
from typing_extensions import Annotated
from typing import List

router = APIRouter()

""" 
************************************In Progress**************************************

@router.post("/login/user/", status_code=201, response_model=schemas.Owner)
async def add_user(user: schemas.OwnerCreate, uow: Annotated[unit_of_work.AbstractUnitOfWork, Depends(get_uow)]):
    try:
        result = services.add_user(user, uow)
    except errors.InvalidDataException:
        raise HTTPException(status_code=404, detail="invalid data")
    except errors.DuplicatedException:
        raise HTTPException(status_code=404, detail="existed data")
    return result


@router.get("/login/owners/{email}/", response_model=schemas.Owner)
async def test(email: str, uow: Annotated[unit_of_work.AbstractUnitOfWork, Depends(get_uow)]):
    try:
        result = services.get_owner_by_email(email, uow)
    except errors.NotFoundException:
        raise HTTPException(status_code=404, detail='Unavailable data')
    return result

************************************In Progress**************************************
"""