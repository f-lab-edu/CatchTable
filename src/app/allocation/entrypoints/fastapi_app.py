from fastapi import FastAPI, HTTPException, Depends
from typing import List, Union
from app.allocation.domain import schemas, model
from app.allocation.service_layer import services, unit_of_work


model.Base.metadata.create_all(bind=unit_of_work.Engine)
app = FastAPI()

def get_uow():
    return unit_of_work.SqlAlchemyUnitOfWork()

@app.post("/owners/", status_code=201, response_model=schemas.Owner)
def add_owner(owner: schemas.Owner, uow=Depends(get_uow)):
    try:
        result = services.add_owner(owner, uow)
    except services.DuplicatedException:
        raise HTTPException(status_code=404, detail="existed data")
    return result


@app.post("/restaurants/", status_code=201, response_model=schemas.Restaurant)
def add_restaurant(owner_id: int, restaurant: schemas.Restaurant, uow=Depends(get_uow)):
    try:
        result = services.add_restaurant(owner_id, restaurant, uow)
    except services.NotFoundException:
        raise HTTPException(status_code=404, detail="invalid id")
    except services.DuplicatedException:
        raise HTTPException(status_code=404, detail="existed data")
    return result



@app.post("/restaurants/{id}/menus/", status_code=201, response_model=schemas.Menu)
def add_menu(id: int, menu: schemas.Menu, uow=Depends(get_uow)):
    try:
        result = services.add_menu(id, menu, uow)
    except services.NotFoundException:
        raise HTTPException(status_code=404, detail="invalid id")
    except services.DuplicatedException:
        raise HTTPException(status_code=404, detail="existed data")
    return result



@app.get("/restaurants/{id}/", response_model=schemas.Restaurant)
def get_restaurant(id: int, uow=Depends(get_uow)):
    result = services.get_restaurant(id, uow)
    if result is None:
        raise HTTPException(status_code=404, detail='Unavailable data')
    return result



@app.get("/restaurants/{id}/menus/", response_model=schemas.Menu)
def get_menu(id: int, uow=Depends(get_uow)):
    result = services.get_menu_for_restaurant(id, uow)
    if result is None:
        raise HTTPException(status_code=404, detail='Unavailable data')
    return result



@app.get("/restaurants/", response_model=List[schemas.Restaurant])
def get_restaurant_list(filter: str, value: Union[str, int], uow=Depends(get_uow)):
    result = services.get_restaurant_list(filter, value, uow)
    if result is None:
        raise HTTPException(status_code=404, detail='Unavailable data')
    return result



@app.put("/restaurants/{id}/", response_model=schemas.Restaurant)
def update_restaurant(id: int, restaurant: schemas.Restaurant, uow=Depends(get_uow)):
    result = services.update_restaurant(id, restaurant, uow)
    if result is None:
        raise HTTPException(status_code=404, detail='Unavailable data')
    return result



@app.put("/restaurants/{id}/menus/", response_model=schemas.Menu)
def update_menu(id: int, menu: schemas.Menu, uow=Depends(get_uow)):
    result = services.update_menu(id, menu, uow)
    if result is None:
        raise HTTPException(status_code=404, detail='Unavailable data')
    return result



@app.delete("/restaurants/{id}/", response_model=schemas.Restaurant)
def delete_restaurant(id: int, uow=Depends(get_uow)):
    result = services.delete_restaurant(id, uow)
    if result is None:
        raise HTTPException(status_code=404, detail='Unavailable data')
    return result



@app.delete("/owners/{id}/", response_model=schemas.Owner)
def delete_owner(id: int, uow=Depends(get_uow)):
    result = services.delete_owner(id, uow)
    if result is None:
        raise HTTPException(status_code=404, detail='Unavailable data')
    return result





