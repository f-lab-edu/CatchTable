from fastapi import APIRouter, HTTPException, Depends
from app.domain import schemas
from app.entrypoints.dependencies import get_uow
from app.service_layer import unit_of_work, errors
from app.service_layer.services import restaurant as services
from typing import List, Union
from typing_extensions import Annotated

router = APIRouter()

@router.post("/restaurants/", status_code=201, response_model=schemas.Restaurant)
async def add_restaurant(owner_id: int, restaurant: schemas.Restaurant, uow: Annotated[
    unit_of_work.AbstractUnitOfWork, Depends(get_uow)]):
    try:
        result = services.add_restaurant(owner_id, restaurant, uow)
    except errors.NotFoundException:
        raise HTTPException(status_code=404, detail="invalid id")
    except errors.InvalidDataException:
        raise HTTPException(status_code=404, detail="invalid data")
    except errors.DuplicatedException:
        raise HTTPException(status_code=404, detail="existed data")
    return result


@router.get("/restaurants/{id}/", response_model=schemas.Restaurant)
async def get_restaurant(id: int, uow: Annotated[unit_of_work.AbstractUnitOfWork, Depends(get_uow)]):
    try:
        result = services.get_restaurant(id, uow)
    except errors.NotFoundException:
        raise HTTPException(status_code=404, detail='Unavailable data')
    return result


@router.get("/restaurants/", response_model=List[schemas.Restaurant])
async def get_restaurant_list(filter: str, value: Union[str, int], uow: Annotated[
    unit_of_work.AbstractUnitOfWork, Depends(get_uow)]):
    try:
        result = services.get_restaurant_list(filter, value, uow)
    except errors.NotFoundException:
        raise HTTPException(status_code=404, detail='Unavailable data')
    return result


@router.put("/restaurants/{id}/", response_model=schemas.Restaurant)
async def update_restaurant(id: int, restaurant: schemas.Restaurant, uow: Annotated[
    unit_of_work.AbstractUnitOfWork, Depends(get_uow)]):
    try:
        result = services.update_restaurant(id, restaurant, uow)
    except errors.NotFoundException:
        raise HTTPException(status_code=404, detail='Unavailable data')
    return result


@router.delete("/restaurants/{id}/", response_model=schemas.Restaurant)
async def delete_restaurant(id: int, uow: Annotated[unit_of_work.AbstractUnitOfWork, Depends(get_uow)]):
    try:
        result = services.delete_restaurant(id, uow)
    except errors.NotFoundException:
        raise HTTPException(status_code=404, detail='Unavailable data')
    return result
