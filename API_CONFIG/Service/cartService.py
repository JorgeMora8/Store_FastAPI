from fastapi import APIRouter
from ..persistences.instances import productService, cartService
from fastapi import Depends
from sqlalchemy.orm import Session
from ..persistences.SQL_alchemy.config_SQLalchemy import get_db
from ..models.PydanticSchema import AddProductSchema
from ..Oauth2.Oauth2_config import current_user

async def showProductInCart(db, user_id): 
    productOnCart = await cartService.getProductInCart(db, user_id)
    for product in productOnCart: 
        product.product
    return productOnCart

async def addProductInCart(db, product_id, user_id): 
    ProductToAddInfo = product_id.dict()
    ProductToAddInfo['client_id'] = user_id
    await cartService.add(db, ProductToAddInfo)
    return ProductToAddInfo


async def removeProductInCart(db, product_id, user_id): 
     await cartService.deleteProductInCart(db, user_id, product_id)