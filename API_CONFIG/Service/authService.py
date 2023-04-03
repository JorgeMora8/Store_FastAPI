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


async def userRegister(db, user): 
    #Register logic
    userData = user.dict()
    newUser = await userService.add(db, userData)
    token = create_token({"user_id": newUser.id})
    
    return {"ACCESS-TOKEN": f"Bearer {token}"}

async def loginUser(db, userLogin): 
    user =  db.query(User).filter(User.email == userLogin.username).first()

    if not user: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalidad credentials")
    
    if user.password != userLogin.password: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")
    
    token = create_token(data={"user_id": user.id})
    return {"ACCES_TOKEN":f"Bearer {token}"}