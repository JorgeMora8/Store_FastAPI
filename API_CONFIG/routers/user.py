from fastapi import APIRouter
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..persistences.SQL_alchemy.config_SQLalchemy import get_db
from ..Oauth2.Oauth2_config import current_user
from ..persistences.instances import reviewService


#On this route is data related with the user logged.
UserRouter = APIRouter(
    prefix="/api/user"
)

@UserRouter.get("/")
async def user(db:Session = Depends(get_db), user = Depends(current_user)): 
    return {
        "first_name":user.first_name, 
        "last_name":user.last_name, 
        "email":user.email
     }

#All reviews from this user.
@UserRouter.get("/reviews")
async def userReviews():
    return "Reviews from the user"
    

@UserRouter.get("/order")
async def userOrder(): 
    return "Order from this review"