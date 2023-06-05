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

# 해당 id가 없어도 불러오는 현상 존재, test 코드 작성해서 exception 잡기
@router.get("/owners/{id}/", response_model=schemas.Owner)
def get_owner(id: int, uow: Annotated[unit_of_work.AbstractUnitOfWork, Depends(get_uow)]):
    result = services.get_owner(id, uow)
    if result is None:
        raise HTTPException(status_code=404, detail='Unavailable data')
    return result


@router.get("/owners/", response_model=List[schemas.Owner])
def get_owner_list(uow: Annotated[unit_of_work.AbstractUnitOfWork, Depends(get_uow)]):
    result = services.get_owner_list(uow)
    if result is None:
        raise HTTPException(status_code=404, detail='Unavailable data')
    return result


@router.delete("/owners/{id}/", response_model=schemas.Owner)
def delete_owner(id: int, uow: Annotated[unit_of_work.AbstractUnitOfWork, Depends(get_uow)]):
    result = services.delete_owner(id, uow)
    if result is None:
        raise HTTPException(status_code=404, detail='Unavailable data')
    return result