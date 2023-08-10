from typing import Union, Dict
from pydantic import BaseModel


class Restaurant(BaseModel):
    name: Union[str, None] = None
    description: Union[str, None] = None
    phone: Union[str, None] = None
    address: Union[str, None] = None
    city: Union[str, None] = None
    kind: Union[str, None] = None

    class Config:
        orm_mode = True


class Owner(BaseModel):
    name: Union[str, None] = None
    phone: Union[str, None] = None
    email: Union[str, None] = None

    class Config:
        orm_mode = True


class OwnerCreate(Owner):
    hashed_password: Union[str, None] = None


class Menu(BaseModel):
    menu: Dict[str, int]

    class Config:
        orm_mode = True
