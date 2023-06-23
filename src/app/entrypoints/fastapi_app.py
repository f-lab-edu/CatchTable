from typing_extensions import Annotated
from fastapi import FastAPI, Depends
# from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.entrypoints.apis import restaurant, menu, owner
from app.entrypoints.dependencies import get_uow

app = FastAPI(dependencies=[Depends(get_uow)])
app.include_router(owner.router)
app.include_router(restaurant.router)
app.include_router(menu.router)

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/")
async def root():
    return {"message": "Welcome to Catch Table"}

# @app.get("/items/")
# async def read_items(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
#     return {"token": form_data}





