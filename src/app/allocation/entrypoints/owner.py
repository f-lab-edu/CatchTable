from fastapi import APIRouter, HTTPException, Depends
from app.allocation.domain import schemas
from app.allocation.entrypoints.dependencies import get_uow
from app.allocation.service_layer import services, errors

router = APIRouter()

@router.post("/owners/", status_code=201, response_model=schemas.Owner)
def add_owner(owner: schemas.Owner, uow=Depends(get_uow)):
    try:
        result = services.add_owner(owner, uow)
    except errors.DuplicatedException:
        raise HTTPException(status_code=404, detail="existed data")
    return result


@router.delete("/owners/{id}/", response_model=schemas.Owner)
def delete_owner(id: int, uow=Depends(get_uow)):
    result = services.delete_owner(id, uow)
    if result is None:
        raise HTTPException(status_code=404, detail='Unavailable data')
    return result