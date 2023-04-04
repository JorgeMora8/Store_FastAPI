### Jorge Andres Mora


## Fast-API "Python" 

The API or application programming interface provides resorces to make the applications or web pages dinamic and with correct functionalitys.
On this project its been reflected a usecase API to a Technology store. Where its compound by users, products and carts. Through the whole process, its been employeed design parents to make the project more dinamic and correct form in case of future adjustemts. 

### Libraries 
```
- bcrypt 
- jose 
- uvicorn 
- fastapi
- sql alchemy
```


### Objects 
On the API, Here is the list of the entities registered on the API. 
 #### Users
 On this entity, its refering the users that will be registered and has access to the whole API and its functionalitys
 ##### Value Objects or Attributes 
 ```
 id: Integer
first_name: Type_value = String
last_name: Type_value = String
email: Type_value = String
password: Type_value = String
```

**Example**
 ```
{
  "id":2,   
  "first_name": "Jorge",
  "last_name": "Mora",
  "email": "jorgeandresmm2002@gmail.com", 
  "password":"**********
}
```

 #### Cart
Its refering to the cart related to one user, where itll contains the products added from the user. Also the user can add more than one product of the same type and also read the products in and delete any of then
 ##### Value Objects or Attributes 
 ```
 id: Integer
client_id: Type_value = String `Related to one user`
products: Type_value = Array 
```

**Example**
 ```
{
"client_id":1, 
client_email:"jorgeandresmm2002@gmail.com", 
products: [{
            "id": 2,
            "category": "phone",
            "name": "Samsung S22 Ultra wide",
            "price": 800
         } ]
}
```

 #### Products
 On this entity, its refering the products avaliable in the store.
 ##### Value Objects or Attributes 
 ```
 id: Integer
name: Type_value = String
price: Type_value = String
category: Type_value = String
```

**Example**
 ```
  {
    "id": 2,
    "category": "phone",
    "name": "Samsung S22 Ultra wide",
    "price": 800
  }
```

 #### Orders
 On this entity, its refering the orders of the product once the user is ready to make the purchase
 ##### Value Objects or Attributes 
 ```
 id: Integer
clientName: Type_value = String
clientEmail: Type_value = String
date: Type_value = String
prods: Type_value = String
total: Type_value = Number
```
**Example**
 ```
{
"id "1679682765789"
"clientName "Jorge"
"clientEmail "jorgeandresmm2002@gmail.com"
"date "Fri Mar 24 2023 14:32:45 GMT-0400 (Venezuela Time)"

"prods":[{
            "id "1e52eb8f-b991-4411-8a6d-2bbc65479021"
            "name "Jamon Don Diego"
            "category "Embutidos"
            "price 150
            "units 2
        }], 
        
"total" :159.98
}
```

 #### Reviews
 The user also has the option to leave a review refering to the store itself. but only the user can delete its own reviews
 ##### Value Objects or Attributes 
 ```
 id: Integer
Author: Type_value = String `User related` 
text: Type_value = String 
```

**Example**
 ```
  {
    "id": 2,
    "user_id": 1,
    "text": "Amazing store, i love it !!"
  }
```
### Routers 
#### Products
- **GET** ***/api/products*** Show the products avaliable in the store
- **GET** ***/api/products/{id}*** show one product searched by the id in the URL
- **POST** ***/api/products*** Add new product in the store (Only admin) 
- **DELETE** ***api/products/{id}*** Delete one product in the store (Only admin)

#### Reviews
- **GET** ***/api/products*** Show the review of the store
- **GET** ***/api/products/{id}*** Show one specific review of the store
- **POST** ***/api/products*** Add new review
- **DELETE** ***api/products/{id}*** Delete one review

#### Cart
- **GET** ***/api/shoppingcart*** Show the products added in the cart
- **POST** ***/api/shoppingcart/{id}*** Add new product in the cart based on the ID
- **DELETE** ***api/shoppingcart/{id}*** Delete one product in the cart based on the ID

#### Auth
- **POST** ***/auth/login*** Login the user
- **POST** ***/auth/register*** Register the user

#### Orders
- **GET** ***/api/orders*** Show the information about the actual order
- **POST** ***/api/orders*** make the order
