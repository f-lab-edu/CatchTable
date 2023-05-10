from fastapi import FastAPI, HTTPException
from typing import List, Union
from app.allocation.domain import schemas, model
from app.allocation.service_layer import services, unit_of_work


model.Base.metadata.create_all(bind=unit_of_work.Engine)
app = FastAPI()


@app.post("/owners/", status_code=201, response_model=schemas.Owner)
def add_owners(owner: schemas.Owner):
    return services.add_owner(owner, unit_of_work.SqlAlchemyUnitOfWork())



@app.post("/restaurants/", status_code=201, response_model=schemas.Restaurant)
def add_restaurant(owner_id: int, restaurant: schemas.Restaurant):
    return services.add_restaurant(owner_id, restaurant, unit_of_work.SqlAlchemyUnitOfWork())



@app.post("/restaurants/{id}/menu/", status_code=201, response_model=schemas.Menu)
def add_menu(id: int, menu: schemas.Menu):
    return services.add_menu(id, menu, unit_of_work.SqlAlchemyUnitOfWork())



@app.get("/restaurants/{id}/", response_model=schemas.Restaurant)
def get_restaurant(id: int):
    result = services.get_restaurant(id, unit_of_work.SqlAlchemyUnitOfWork())
    if result is None:
        raise HTTPException(status_code=404, detail='Unavailable data')
    return result



@app.get("/restaurants/{id}/menu/", response_model=schemas.Menu)
def get_menu(id: int):
    result = services.get_menu_for_restaurant(id, unit_of_work.SqlAlchemyUnitOfWork())
    if result is None:
        raise HTTPException(status_code=404, detail='Unavailable data')
    return result



@app.get("/restaurants/", response_model=List[schemas.Restaurant])
def get_restaurant_list(filter: str, value: Union[str, int]):
    result = services.get_restaurant_list(filter, value, unit_of_work.SqlAlchemyUnitOfWork())
    if result is None:
        raise HTTPException(status_code=404, detail='Unavailable data')
    return result



@app.put("/restaurants/{id}/", response_model=schemas.Restaurant)
def update_restaurant(id: int, restaurant: schemas.Restaurant):
    result = services.update_restaurant(id, restaurant, unit_of_work.SqlAlchemyUnitOfWork())
    if result is None:
        raise HTTPException(status_code=404, detail='Unavailable data')
    return result



@app.put("/restaurants/{id}/menu/", response_model=schemas.Menu)
def update_menu(id: int, menu: schemas.Menu):
    result = services.update_menu(id, menu, unit_of_work.SqlAlchemyUnitOfWork())
    if result is None:
        raise HTTPException(status_code=404, detail='Unavailable data')
    return result



@app.delete("/restaurants/{id}/", response_model=schemas.Restaurant)
def delete_restaurant(id: int):
    result = services.delete_restaurant(id, unit_of_work.SqlAlchemyUnitOfWork())
    if result is None:
        raise HTTPException(status_code=404, detail='Unavailable data')
    return result





