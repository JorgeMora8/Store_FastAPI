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


AuthRouter = APIRouter()

@AuthRouter.post("/register")
async def register(user:UserSchema, db:Session = Depends(get_db)): 
    try: 
        token = await userRegister(db, user)
        return token
    except Exception as error: 
        print(error)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Error on saving the user")


@AuthRouter.post("/login")
async def login(userLogin: OAuth2PasswordRequestForm = Depends() ,db:Session = Depends(get_db)): 
    try: 
        token = await loginUser(db, userLogin)
        return token
    except Exception as error: 
        print(error)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="error login in the user")
    
