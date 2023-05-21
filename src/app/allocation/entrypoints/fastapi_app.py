from fastapi import FastAPI
from app.allocation.entrypoints import owner, restaurant, menu


app = FastAPI()
app.include_router(owner.router)
app.include_router(restaurant.router)
app.include_router(menu.router)

@app.get("/")
def root():
    return {"message": "Welcome to Catch Table"}

