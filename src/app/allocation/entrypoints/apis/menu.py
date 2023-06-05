from fastapi import APIRouter, HTTPException, Depends
from app.allocation.domain import schemas
from app.allocation.entrypoints.dependencies import get_uow
from app.allocation.service_layer import errors
from app.allocation.service_layer.services import menu as services

router = APIRouter()

@router.post("/restaurants/{id}/menus/", status_code=201, response_model=schemas.Menu)
def add_menu(id: int, menu: schemas.Menu, uow=Depends(get_uow)):
    try:
        result = services.add_menu(id, menu, uow)
    except errors.NotFoundException:
        raise HTTPException(status_code=404, detail="invalid id")
    except errors.DuplicatedException:
        raise HTTPException(status_code=404, detail="existed data")
    return result


@router.get("/restaurants/{id}/menus/", response_model=schemas.Menu)
def get_menu(id: int, uow=Depends(get_uow)):
    result = services.get_menu_for_restaurant(id, uow)
    if result is None:
        raise HTTPException(status_code=404, detail='Unavailable data')
    return result


@router.put("/restaurants/{id}/menus/", response_model=schemas.Menu)
def update_menu(id: int, menu: schemas.Menu, uow=Depends(get_uow)):
    result = services.update_menu(id, menu, uow)
    if result is None:
        raise HTTPException(status_code=404, detail='Unavailable data')
    return result