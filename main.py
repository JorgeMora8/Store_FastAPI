from fastapi import FastAPI
from API_CONFIG.persistences.SQL_alchemy.config_SQLalchemy import base, engine

from API_CONFIG.routers.store import StoreRouter
from API_CONFIG.routers.auth import AuthRouter
from API_CONFIG.routers.cart import ShoppingCartRouter
from API_CONFIG.routers.order import OrderRouter
from API_CONFIG.routers.reviews import ReviewRouter
from API_CONFIG.routers.user import UserRouter

def create_table(): 
    base.metadata.create_all(bind=engine)

create_table()

app = FastAPI()

#Adding FastAPI routers
app.include_router(StoreRouter)
app.include_router(AuthRouter)
app.include_router(OrderRouter)
app.include_router(ShoppingCartRouter)
app.include_router(ReviewRouter)
app.include_router(UserRouter)


app.get("/")
# async def HomePage(): 
#     return {
#         "Store_route": "/api/store", 
#         "Review_router":"api/review", 
#         ""
#     }