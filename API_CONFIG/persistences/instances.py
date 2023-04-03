from .DAO import DAO
from ..models.PostgresModel import Product, User, Review, ProductOnCart


productService = DAO(Product)
userService = DAO(User)
reviewService = DAO(Review)
cartService = DAO(ProductOnCart)