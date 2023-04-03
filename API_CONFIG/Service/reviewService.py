from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..persistences.SQL_alchemy.config_SQLalchemy import get_db
from ..models.PostgresModel import Product
from ..models.PydanticSchema import ProductSchema
from ..persistences.instances import productService
from ..Oauth2.Oauth2_config import current_user
from ..persistences.instances import reviewService
from ..Validations.reviews.SameUser import sameUser

async def reviewList(db): 
    return await reviewService.get_all(db)

async def getReviewById(db, id): 
    return await reviewService.get_by_id(db, id)


async def newReview(db, data, user_id): 
    addReview = data.dict()
    addReview['user_id'] = user_id
    await reviewService.add(db, addReview)
    return addReview

async def deleteOneReview(db, review_id, user_id): 
    review = await reviewService.get_by_id(db, review_id) 

    #Validation
    sameUser(review.user_id, user_id)

    await reviewService.delete(db, review_id)
    return "Review deleted"