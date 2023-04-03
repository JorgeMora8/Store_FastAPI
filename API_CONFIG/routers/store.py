from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..persistences.SQL_alchemy.config_SQLalchemy import get_db
from ..models.PostgresModel import Product
from ..models.PydanticSchema import ProductSchema
from ..persistences.instances import productService
from ..Oauth2.Oauth2_config import current_user
from ..Service.storeService import *


StoreRouter = APIRouter(
    prefix="/api/products"
)

@StoreRouter.get("/")
async def products(db:Session = Depends(get_db), user = Depends(current_user)): 
    try:
        return await getProducts(db)
    except Exception: 
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=Exception)
    

@StoreRouter.get("/{id}")
async def product(id:int, db:Session = Depends(get_db), user = Depends(current_user)): 
    try:
        return await productById(db, id)
    except Exception: 
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=Exception)

@StoreRouter.post("/")
async def addProduct( product: ProductSchema ,db:Session = Depends(get_db), user = Depends(current_user)): 
    try: 
        return await newProduct(db, product)
    except Exception: 
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=Exception)
    
@StoreRouter.delete("/{id}")
async def deleteProduct(id:int, user = Depends(current_user), db:Session = Depends(get_db)): 
    try: 
        await deleteOneProduct(db, id)
    except Exception: 
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=Exception)

