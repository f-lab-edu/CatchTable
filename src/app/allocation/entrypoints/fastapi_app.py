from fastapi import FastAPI, HTTPException
from typing import List
from app.allocation.adapters import orm
from app.allocation.domain import schema
from app.allocation.service_layer import services, unit_of_work

orm.start_mappers()
orm.metadata.create_all(bind=unit_of_work.Engine)
app = FastAPI()


@app.post("/owners/", status_code=201)
def create_owners(owner: schema.Owner):
    services.add_owner(owner, unit_of_work.SqlAlchemyUnitOfWork())


@app.post("/restaurants/", status_code=201)
def create_restaurant(owner_id: int, restaurant: schema.Restaurant):
    services.add_restaurant(owner_id, restaurant, unit_of_work.SqlAlchemyUnitOfWork())


@app.post("/restaurants/{restaurant_id}/menu/", status_code=201)
def create_menu(restaurant_id: int, menu: schema.Menu):
    services.add_menu(restaurant_id, menu, unit_of_work.SqlAlchemyUnitOfWork())


@app.get("/restaurants/", response_model=List[schema.Restaurant])
def get_restaurant_by_filter(filter: str, value: str):
    restaurants = services.get_restaurant(filter,
                                          value,
                                          unit_of_work.SqlAlchemyUnitOfWork())
    if restaurants is None:
        raise HTTPException(status_code=404, detail='Unavailable Filter')
    return restaurants

"""In progress
@app.put("/owners/{owner_id}/restaurants/{restaurant_id}/", response_model=schema.Restaurant)
def edit_restaurant(restaurant_id: int, restaurant: schema.Restaurant):
"""


