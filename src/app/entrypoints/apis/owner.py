from fastapi import APIRouter, HTTPException, Depends
from app.domain import schemas
from app.entrypoints.dependencies import get_uow
from app.service_layer import unit_of_work, errors
from app.service_layer.services import owner as services
from typing_extensions import Annotated
from typing import List

router = APIRouter()


@router.post("/owners/", status_code=201, response_model=schemas.Owner)
async def add_owner(owner: schemas.Owner, uow: Annotated[unit_of_work.AbstractUnitOfWork, Depends(get_uow)]):
    try:
        result = services.add_owner(owner, uow)
    except errors.InvalidDataException:
        raise HTTPException(status_code=404, detail="invalid data")
    except errors.DuplicatedException:
        raise HTTPException(status_code=404, detail="existed data")
    return result


@router.get("/owners/{id}/", response_model=schemas.Owner)
async def get_owner(id: int, uow: Annotated[unit_of_work.AbstractUnitOfWork, Depends(get_uow)]):
    try:
        result = services.get_owner(id, uow)
    except errors.NotFoundException:
        raise HTTPException(status_code=404, detail='Unavailable data')
    return result


@router.get("/owners/", response_model=List[schemas.Owner])
async def get_owner_list(uow: Annotated[unit_of_work.AbstractUnitOfWork, Depends(get_uow)]):
    try:
        result = services.get_owner_list(uow)
    except errors.NotFoundException:
        raise HTTPException(status_code=404, detail='Unavailable data')
    return result


@router.put("/owners/{id}/", response_model=schemas.Owner)
async def update_owner(id: int, owner: schemas.Owner, uow: Annotated[unit_of_work.AbstractUnitOfWork, Depends(get_uow)]):
    try:
        result = services.update_owner(id, owner, uow)
    except errors.NotFoundException:
        raise HTTPException(status_code=404, detail='Unavailable data')
    return result


@router.delete("/owners/{id}/", response_model=schemas.Owner)
async def delete_owner(id: int, uow: Annotated[unit_of_work.AbstractUnitOfWork, Depends(get_uow)]):
    try:
        result = services.delete_owner(id, uow)
    except errors.NotFoundException:
        raise HTTPException(status_code=404, detail='Unavailable data')
    return result