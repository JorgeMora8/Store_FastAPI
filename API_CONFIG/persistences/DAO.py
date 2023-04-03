

class DAO: 
    def __init__(self, table): 
        self.table = table

    async def get_all(self, db): 
        return db.query(self.table).all()
    
    async def get_by_id(self, db, id): 
        return db.query(self.table).filter(self.table.id == id).first()
    
    
    async def get_by_user(self, db, user_id): 
        return db.query(self.table).filter(self.table.id == user_id)
    
    async def add(self, db, data):
        item = self.table(**data)
        db.add(item)
        db.commit()
        db.refresh(item)
        return item
    
    async def getProductInCart(self, db, client_id): 
        return db.query(self.table).filter(self.table.client_id == client_id).all()

    async def deleteProductInCart(self, db, client_id, product_id): 
        product =  db.query(self.table).filter(self.table.client_id == client_id).filter(self.table.id == product_id)
        product.delete()
        db.commit()
    
    async def deleteAllProduct(self, db, client_id): 
        products = db.query(self.table).filter(self.table.client_id == client_id)
        products.delete()
        db.commit()


    async def delete(self, db, id): 
        item = db.query(self.table).filter(self.table.id == id)
        item.delete()
        db.commit()










    # async def update(self, db, id, data): 
    #     #Check if its need the use the .first() or not
    #     item = db.query(self.table).filter(self.table.id == id).first()
    #     item.update(data, synchronize_session=False)
    #     print(item.id)
    #     # db.commit()

    #     # return item.dict()