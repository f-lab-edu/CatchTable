from fastapi import APIRouter, HTTPException, Depends
from app.domain import schemas
from app.entrypoints.dependencies import get_uow
from app.service_layer import errors
from app.service_layer.services import menu as services

router = APIRouter()

@router.post("/restaurants/{id}/menus/", status_code=201, response_model=schemas.Menu)
async def add_menu(id: int, menu: schemas.Menu, uow=Depends(get_uow)):
    try:
        result = services.add_menu(id, menu, uow)
    except errors.NotFoundException:
        raise HTTPException(status_code=404, detail="invalid id")
    except errors.DuplicatedException:
        raise HTTPException(status_code=404, detail="existed data")
    return result


@router.get("/restaurants/{id}/menus/", response_model=schemas.Menu)
async def get_menu(id: int, uow=Depends(get_uow)):
    try:
        result = services.get_menu_for_restaurant(id, uow)
    except errors.NotFoundException:
        raise HTTPException(status_code=404, detail='Unavailable data')
    return result


@router.put("/restaurants/{id}/menus/", response_model=schemas.Menu)
async def update_menu(id: int, menu: schemas.Menu, uow=Depends(get_uow)):
    try:
        result = services.update_menu(id, menu, uow)
    except errors.NotFoundException:
        raise HTTPException(status_code=404, detail='Unavailable data')
    return result