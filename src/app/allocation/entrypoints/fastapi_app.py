from fastapi import FastAPI, HTTPException
from typing import List, Union
from app.allocation.adapters import orm
from app.allocation.domain import schemas
from app.allocation.service_layer import services, unit_of_work


orm.start_mappers()
orm.metadata.create_all(bind=unit_of_work.Engine)
app = FastAPI()


@app.post("/owners/", status_code=201)
def create_owners(owner: schemas.Owner):
    services.add_owner(owner, unit_of_work.SqlAlchemyUnitOfWork())


@app.post("/restaurants/", status_code=201)
def create_restaurant(owner_id: int, restaurant: schemas.Restaurant):
    services.add_restaurant(owner_id, restaurant, unit_of_work.SqlAlchemyUnitOfWork())


@app.post("/restaurants/{restaurant_id}/menu/", status_code=201)
def create_menu(restaurant_id: int, menu: schemas.Menu):
    services.add_menu(restaurant_id, menu, unit_of_work.SqlAlchemyUnitOfWork())


@app.get("/restaurants/", response_model=List[schemas.Restaurant])
def get_restaurants_by_filter(filter: str, value: Union[str, int]):
    restaurants = services.get_restaurants(filter,
                                          value,
                                          unit_of_work.SqlAlchemyUnitOfWork())
    if restaurants is None:
        raise HTTPException(status_code=404, detail='Unavailable Filter')
    return restaurants


@app.put("/restaurants/{restaurant_id}/", response_model=schemas.Restaurant)
def update_restaurant(restaurant_id: int, restaurant: schemas.Restaurant):
    return services.update_restaurant(restaurant_id,
                                      restaurant,
                                      unit_of_work.SqlAlchemyUnitOfWork())


@app.delete("/restaurants/{restaurant_id}/")
def delete_restaurant(restaurant_id: int):
    return services.delete_restaurant(restaurant_id,
                                      unit_of_work.SqlAlchemyUnitOfWork())



""" 
1. menu 관련된 Post, Get, Put  메소드 관련 질문
2. 아직 예외 처리가 안 되어있음
"""


