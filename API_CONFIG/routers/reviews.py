from fastapi import APIRouter
from ..persistences.instances import reviewService
from sqlalchemy.orm import Session
from fastapi import Depends
from ..persistences.SQL_alchemy.config_SQLalchemy import get_db
from ..Oauth2.Oauth2_config import current_user
from ..models.PydanticSchema import ReviewSchema
from ..Validations.reviews.SameUser import sameUser
from ..Service.reviewService import *
from fastapi import HTTPException, status


ReviewRouter = APIRouter(
    prefix="/api/reviews"
)

@ReviewRouter.get("/")
async def getReviews(db:Session = Depends(get_db), user = Depends(current_user)): 
    try: 
        reviews = await reviewList(db)
        return reviews
    except Exception: 
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=Exception)

@ReviewRouter.get("/{id}")
async def getById(id:int, db:Session = Depends(get_db), user = Depends(current_user)): 
    try: 
        review = await getReviewById(db, id)
        return review
    except Exception: 
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=Exception)

@ReviewRouter.post("/")
async def addReview(reviewData:ReviewSchema ,db:Session = Depends(get_db), user = Depends(current_user)):
    try: 
        review = await newReview(db, reviewData, user.id)
        return review
    except Exception: 
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=Exception)

@ReviewRouter.delete("/{id}")
async def deleteReview(id:int,db:Session = Depends(get_db), user = Depends(current_user)):
    try: 
        
        await deleteOneReview(db, id, user.id)
    except Exception as error: 
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"There was an error {error}")