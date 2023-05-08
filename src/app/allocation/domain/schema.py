from typing import List, Union, Dict
from pydantic import BaseModel



class Restaurant(BaseModel):
    name: str
    description: Union[str, None] = None
    phone: str
    address: str
    city: str
    kind: str
    class Config:
        orm_mode = True

class Owner(BaseModel):
    name: str
    phone: str
    email: str
    class Config:
        orm_mode= True

class Menu(BaseModel):
    menu: Dict[str, int]
    class Config:
        orm_mode= True

