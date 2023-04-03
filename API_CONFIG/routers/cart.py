from fastapi import APIRouter
from ..persistences.instances import productService, cartService
from fastapi import Depends
from sqlalchemy.orm import Session
from ..persistences.SQL_alchemy.config_SQLalchemy import get_db
from ..models.PydanticSchema import AddProductSchema
from ..Oauth2.Oauth2_config import current_user
from ..Service.cartService import *
from fastapi import HTTPException, status


ShoppingCartRouter = APIRouter(
    prefix="/api/shoppingcart"
)

@ShoppingCartRouter.get("/")
async def getCart(db:Session = Depends(get_db), user = Depends(current_user)): 
    try:
        productsOnCart = await showProductInCart(db, user.id)
        return productsOnCart
    except Exception as Error: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Error getting the data")

@ShoppingCartRouter.post("/")
async def addProduct( productId: AddProductSchema ,db:Session = Depends(get_db), user = Depends(current_user)): 
    try: 
        productAdded = await addProductInCart(db, productId, user.id)
        return productAdded
    except Exception as error: 
        print(error)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Error adding the product")
    


@ShoppingCartRouter.delete("/{id}")
async def removeProduct(id:int, db:Session = Depends(get_db), user = Depends(current_user)): 
    try:
        await cartService.deleteProductInCart(db, user.id, id )
    except Exception as error: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="There was an error")


