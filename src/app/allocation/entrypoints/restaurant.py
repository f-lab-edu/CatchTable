from fastapi import APIRouter, HTTPException, Depends
from app.allocation.domain import schemas
from app.allocation.entrypoints.dependencies import get_uow
from app.allocation.service_layer import services, errors
from typing import List, Union

router = APIRouter()

@router.post("/restaurants/", status_code=201, response_model=schemas.Restaurant)
def add_restaurant(owner_id: int, restaurant: schemas.Restaurant, uow=Depends(get_uow)):
    try:
        result = services.add_restaurant(owner_id, restaurant, uow)
    except errors.NotFoundException:
        raise HTTPException(status_code=404, detail="invalid id")
    except errors.DuplicatedException:
        raise HTTPException(status_code=404, detail="existed data")
    return result


@router.get("/restaurants/{id}/", response_model=schemas.Restaurant)
def get_restaurant(id: int, uow=Depends(get_uow)):
    result = services.get_restaurant(id, uow)
    if result is None:
        raise HTTPException(status_code=404, detail='Unavailable data')
    return result


@router.get("/restaurants/", response_model=List[schemas.Restaurant])
def get_restaurant_list(filter: str, value: Union[str, int], uow=Depends(get_uow)):
    result = services.get_restaurant_list(filter, value, uow)
    if result is None:
        raise HTTPException(status_code=404, detail='Unavailable data')
    return result


@router.put("/restaurants/{id}/", response_model=schemas.Restaurant)
def update_restaurant(id: int, restaurant: schemas.Restaurant, uow=Depends(get_uow)):
    result = services.update_restaurant(id, restaurant, uow)
    if result is None:
        raise HTTPException(status_code=404, detail='Unavailable data')
    return result


@router.delete("/restaurants/{id}/", response_model=schemas.Restaurant)
def delete_restaurant(id: int, uow=Depends(get_uow)):
    result = services.delete_restaurant(id, uow)
    if result is None:
        raise HTTPException(status_code=404, detail='Unavailable data')
    return result
