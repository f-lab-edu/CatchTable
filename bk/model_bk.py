from typing import Dict

class Restaurant:
    def __init__(self,
                 name: str,
                 owner_id: int,
                 description: str,
                 phone: str,
                 address: str,
                 city: str,
                 kind: str
                 ):

        self.name = name
        self.owner_id = owner_id
        self.description= description
        self.phone= phone
        self.address= address
        self.city= city
        self.kind= kind

class Menu:
    def __init__(self,
                 menu: Dict[str, int],
                 restaurant_id: int):
        self.menu = menu
        self.restaurant_id = restaurant_id

class Owner:
    def __init__(self,
                 name: str,
                 phone: str,
                 email: str,
                 ):
        self.name = name
        self.phone = phone
        self.email = email



