from jose import JWTError, jwt
from datetime import timedelta, datetime
# from ..models.PydanticSchema import 
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from ..persistences.SQL_alchemy.config_SQLalchemy import *
from ..persistences.instances import userService, User


Oauth2_schema = OAuth2PasswordBearer(tokenUrl="login")

#Token paramters 
SECRET_KEY = "programming"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_TIME = 60

def create_token(data:dict): 
    print(data)
    # Get the data to encode
    encode = data.copy()
    expiry_time = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_TIME)
    encode.update({"exp": expiry_time})
    # encode.update()

    token = jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)
    return token


def verify_token(token, credential_expections): 
    try: 
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("user_id")
        if user_id is None: 
            raise credential_expections
        return user_id
               
    except JWTError: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Signature has expired")


async def current_user(token:str = Depends(Oauth2_schema), db:Session = Depends(get_db)):
    # try: 
    credential_expections = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect token")
    decodeToken = verify_token(token, credential_expections)
        # user = await userService.
    user = db.query(User).filter(User.id == decodeToken).first()
    if not user: 
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalidad token, no user related")
    # return verify_token(token, credential_expections)
    return user