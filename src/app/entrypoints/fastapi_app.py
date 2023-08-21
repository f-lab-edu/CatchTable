from fastapi import FastAPI, Depends
from app.entrypoints.apis import restaurant, menu, owner, login, registration
from app.entrypoints.dependencies import get_uow


app = FastAPI(dependencies=[Depends(get_uow)])
app.include_router(owner.router)
app.include_router(restaurant.router)
app.include_router(menu.router)
app.include_router(login.router)
app.include_router(registration.router)


@app.get("/")
async def root():
    return {"message": "Welcome to Catch Table"}
