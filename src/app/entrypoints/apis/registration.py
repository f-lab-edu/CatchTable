from fastapi import APIRouter, HTTPException, Depends
from app.domain import schemas
from app.entrypoints.dependencies import get_uow
from app.service_layer import unit_of_work, errors
from app.service_layer.services import registration
from typing_extensions import Annotated


router = APIRouter()


@router.post("/registration/", status_code=201, response_model=schemas.Owner)
async def add_user(user: schemas.OwnerCreate, uow: Annotated[unit_of_work.AbstractUnitOfWork, Depends(get_uow)]):
    try:
        return registration.add_user(user, uow)
    except errors.DuplicatedException:
        raise HTTPException(status_code=404, detail="existed data")
