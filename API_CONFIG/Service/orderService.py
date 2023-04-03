from fastapi import APIRouter, HTTPException, status
from ..models.PydanticSchema import *
from ..persistences.instances import userService
from ..Oauth2.Oauth2_config import create_token
from ..persistences.SQL_alchemy.config_SQLalchemy import *
from sqlalchemy.orm import Session
from fastapi import Depends
from ..models.PostgresModel import * 
from ..Oauth2.Oauth2_config import create_token
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from ..Service.authService import *
from ..Service.cartService import cartService

async def makeProductsOrder(db, user_id): 
    await cartService.deleteAllProduct(db, user_id)