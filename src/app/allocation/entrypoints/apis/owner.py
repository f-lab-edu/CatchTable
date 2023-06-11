from fastapi import APIRouter, HTTPException, Depends
from app.allocation.domain import schemas
from app.allocation.entrypoints.dependencies import get_uow
from app.allocation.service_layer import errors, unit_of_work
from app.allocation.service_layer.services import owner as services
from typing_extensions import Annotated
from typing import List, Union

router = APIRouter()


@router.post("/owners/", status_code=201, response_model=schemas.Owner)
def add_owner(owner: schemas.Owner, uow: Annotated[unit_of_work.AbstractUnitOfWork, Depends(get_uow)]):
    try:
        result = services.add_owner(owner, uow)
    except errors.InvalidDataException:
        raise HTTPException(status_code=404, detail="invalid data")
    except errors.DuplicatedException:
        raise HTTPException(status_code=404, detail="existed data")
    return result


@router.get("/owners/{id}/", response_model=schemas.Owner)
def get_owner(id: int, uow: Annotated[unit_of_work.AbstractUnitOfWork, Depends(get_uow)]):
    try:
        result = services.get_owner(id, uow)
    except errors.NotFoundException:
        raise HTTPException(status_code=404, detail='Unavailable data')
    return result


@router.get("/owners/", response_model=List[schemas.Owner])
def get_owner_list(uow: Annotated[unit_of_work.AbstractUnitOfWork, Depends(get_uow)]):
    try:
        result = services.get_owner_list(uow)
    except errors.NotFoundException:
        raise HTTPException(status_code=404, detail='Unavailable data')
    return result


@router.put("/owners/{id}/", response_model=schemas.Owner)
def update_owner(id: int, owner: schemas.Owner, uow: Annotated[unit_of_work.AbstractUnitOfWork, Depends(get_uow)]):
    try:
        result = services.update_owner(id, owner, uow)
    except errors.NotFoundException:
        raise HTTPException(status_code=404, detail='Unavailable data')
    return result


@router.delete("/owners/{id}/", response_model=schemas.Owner)
def delete_owner(id: int, uow: Annotated[unit_of_work.AbstractUnitOfWork, Depends(get_uow)]):
    try:
        result = services.delete_owner(id, uow)
    except errors.NotFoundException:
        raise HTTPException(status_code=404, detail='Unavailable data')
    return result