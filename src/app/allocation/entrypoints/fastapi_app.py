from fastapi import FastAPI, Depends
from app.allocation.entrypoints.apis import menu, restaurant, owner
from app.allocation.entrypoints.dependencies import get_uow

app = FastAPI(dependencies=[Depends(get_uow)])
app.include_router(owner.router)
app.include_router(restaurant.router)
app.include_router(menu.router)

@app.get("/")
async def root():
    return {"message": "Welcome to Catch Table"}





