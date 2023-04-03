from sqlalchemy import Column, Integer, String, ForeignKey
from ..persistences.SQL_alchemy.config_SQLalchemy import base
from sqlalchemy.orm import relationship

class Product(base): 
    __tablename__ = "product"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    price = Column(Integer, nullable=False)

    class Config: 
        orm_mode = True

class User(base): 
    __tablename__ = "user"
    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)

    class Config: 
        orm_mode = True


#Map thought the table, searching with the ID user and bring all the products related with the user ID
class ProductOnCart(base):
    __tablename__ = "cart" 
    id = Column(Integer, autoincrement=True, primary_key=True)
    client_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    product_id = Column(Integer, ForeignKey("product.id", ondelete="CASCADE"))
    product = relationship("Product", backref="user")

    class Config: 
        orm_mode = True

class Review(base): 
    __tablename__ = "review"
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"))
    text = Column(String, nullable=False)

    class Config: 
        orm_mode = True
    