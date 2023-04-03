from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..persistences.SQL_alchemy.config_SQLalchemy import get_db
from ..models.PostgresModel import Product
from ..models.PydanticSchema import ProductSchema
from ..persistences.instances import productService
from ..Oauth2.Oauth2_config import current_user


async def getProducts(db): 
        products = await productService.get_all(db)
        return products

async def productById(db, id): 
    product = await productService.get_by_id(db, id)
    return product


async def newProduct(db, data): 
    await productService.add(db, data.dict())
    return data

async def deleteOneProduct(db, productId): 
    await productService.delete(db, productId)
