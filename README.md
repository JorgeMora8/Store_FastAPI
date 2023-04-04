### Jorge Andres Mora


## Fast-API "Python" 

The API or application programming interface provides resorces to make the applications or web pages dinamic and with correct functionalitys.
On this project its been reflected a usecase API to a Technology store. Where its compound by users, products and carts. Through the whole process, its been employeed design parents to make the project more dinamic and correct form in case of future adjustemts. 

#### Warning
***Make sure to have Node.js installed on your machine. [Link](https://nodejs.org/en)***

### Libraries 
```
- bcrypt 
- jose 
- uvicorn 
- fastapi
- sql alchemy
```


## The construction of the API. 
Building the Market API, was employeed different design pattern. 
***Design patterns are typical solutions to common problems
in software design***. 
It can appreciate a Layer Arquitecture, where the goal is to seperate responsabilites and give the functionalities to be attended to each layers.
Its conform by 3 layers (four in total if we count the frontend part "Presentation Layer")
#### Controller Layer
#### Service Layer 
#### Respository Layer


### Objects 
On the API, Here is the list of the entities registered on the API. 
 #### Users
 On this entity, its refering the users that will be registered and has access to the whole API and its functionalitys
 ##### Value Objects or Attributes 
 ```
 id: String (Source= UUID)
first_name: Type_value = String
last_name: Type_value = String
email: Type_value = String
password: Type_value = String
```

**Example**
 ```
{
    "_id": 6424f6170bdb38cf9b69688b
    "id": "1680143895809"
    "name": "Jorge"
    "lastname": "Mora"
    "email" "jorgeandresmm2002@gmail.com"
    "password": "$2b$10$H0haSQCz9WRvhi0o8wipEe5QIDM5pQYAfkV6hoSd83n.ulgLPgzAq"
    "admin": true
    "card": 0
    "__v": 0
}
```

 #### Cart
Its refering to the cart related to one user, where itll contains the products added from the user. Also the user can add more than one product of the same type and also read the products in and delete any of then
 ##### Value Objects or Attributes 
 ```
 id: String (Source= UUID)
client_id: Type_value = String `Related to one user`
products: Type_value = Array 
```

**Example**
 ```
{
    "_id": 6424f6170bdb38cf9b69688b
    "id": "1680143895809"
    "name": "Jorge"
    "lastname": "Mora"
    "email" "jorgeandresmm2002@gmail.com"
    "password": "$2b$10$H0haSQCz9WRvhi0o8wipEe5QIDM5pQYAfkV6hoSd83n.ulgLPgzAq"
    "admin": true
    "card": 0
    "__v": 0
}
```

 #### Products
 On this entity, its refering the products avaliable in the store.
 ##### Value Objects or Attributes 
 ```
 id: String (Source= UUID)
name: Type_value = String
price: Type_value = String
category: Type_value = String
```

**Example**
 ```
  {
    "id": "5d01dc54-5ee6-459c-9bc4-17c22d16b00b",
    "name": "Oats Quaker & Mousli",
    "category": "Cereals",
    "price": 8.99,
    "units": 50,
    "image": "https://walmartcr.vtexassets.com/arquivos/ids/366669/Avena-Quaker-Mosh-Hojuelas-300gr-1-26043.jpg?v=638052575651430000"
  }
```

 #### Orders
 On this entity, its refering the orders of the product once the user is ready to make the purchase
 ##### Value Objects or Attributes 
 ```
 id: String (Source= UUID)
clientName: Type_value = String
clientEmail: Type_value = String
date: Type_value = String
prods: Type_value = String
total: Type_value = Number
```
**Example**
 ```
{

"_id 641deccd42c69b89b45076db
"id "1679682765789"
"clientName "Jorge"
"clientEmail "jorgeandresmm2002@gmail.com"
"date "Fri Mar 24 2023 14:32:45 GMT-0400 (Venezuela Time)"

"prods":{
        "id "1e52eb8f-b991-4411-8a6d-2bbc65479021"
        "name "Jamon Don Diego"
        "category "Embutidos"
        "price 150
        "units 2

id  "eb3991cd-206c-42ee-b081-519cc8930f72"
name "Migurt 500ml"
category "Yogurt"
price 9.98
units 7
total 159.98
__v 0
}
```

 #### Reviews
 The user also has the option to leave a review refering to the store itself. but only the user can delete its own reviews
 ##### Value Objects or Attributes 
 ```
 id: String (Source= UUID)
Author: Type_value = String `User related` 
text: Type_value = String 
```

**Example**
 ```
{
    "_id": 6419c6de0a6da9d027b2e65e
    "id": "1679410910541"
    "author": "jorge"
    "text": "second review"
    "__v": 0
}
```
### Routers 
#### Products
- **GET** ***/api/products*** Show the products avaliable in the store
- **GET** ***/api/products/{id}*** show one product searched by the id in the URL
- **POST** ***/api/products*** Add new product in the store (Only admin)
- **PUT** ***api/products/{id}*** Update a new product base on the ID added on the URL. (Only admin) 
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
