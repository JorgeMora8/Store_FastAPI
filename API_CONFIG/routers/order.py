from fastapi import APIRouter
from ..persistences.instances import productService, cartService
from fastapi import Depends
from sqlalchemy.orm import Session
from ..persistences.SQL_alchemy.config_SQLalchemy import get_db
from ..models.PydanticSchema import AddProductSchema
from ..Oauth2.Oauth2_config import current_user
from ..Service.orderService import *

OrderRouter = APIRouter(
    prefix="/api/order"
)

@OrderRouter.get("/")
async def infoOrder(): 
    return "Info about the order"

@OrderRouter.post("/")
async def makeOrder(db:Session = Depends(get_db), user = Depends(current_user)):
    # await cartService.deleteAllProduct(db, user.id)
    # return "deleted"

    try: 
        await makeProductsOrder(db, user.id)
        return "The order was send!!"
    except Exception as Error: 
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="We couldnt make the order")
