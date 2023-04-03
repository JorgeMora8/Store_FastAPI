from pydantic import BaseModel, EmailStr, validator
from ..Validations.products.pydanticValidators import emptySpace, noQuanity

class ProductSchema(BaseModel): 
    name:str
    category:str
    price:int

    @validator("price")
    def price_cannot_be_zero(cls, value): 
        if value <= 0: 
            raise ValueError("The price cant be zero or lower")
        return value
    
    @validator("name")
    def name_cant_be_empty(cls, name): 
        if len(name) == 0: 
            raise ValueError("The name space cant be empty")
        return name
    
    @validator("category")
    def category_cant_be_empty(cls, category): 
        if len(category) == 0: 
            raise ValueError("The category space cant be empty")
        return category


class UserSchema(BaseModel): 
    first_name:str
    last_name:str
    email: EmailStr
    password: str

class ReviewSchema(BaseModel): 
    text:str

class OrderSchema(BaseModel): 
    client_email:EmailStr
    date:str
    product: list
    total:int


class UserLoginSchema(BaseModel): 
    email:str
    password:str

class AddProductSchema(BaseModel): 
    product_id:int