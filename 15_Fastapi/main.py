
from fastapi import FastAPI,HTTPException
from typing import Optional
from pydantic import BaseModel,Field

app = FastAPI()


# @app.get("/")
# def home():
#     return {"message": "Hello FastAPI"}


# # @app.get("/products")
# # def get_products():
# #     return {"products": ["Laptop", "Mouse", "Keyboard"]}


# # @app.get("/users")
# # def get_users():
# #     return {"users": ["Ali", "Ahmed", "Sara"]}

# @app.get('/books/{book_id}')
# def books(book_id:int):
#     return {'book':book_id,
#             'title':'John'}


# @app.get('/employees/{employee_id}')
# def books(employee_id:int):
#     return {'Employee_id':employee_id,
#             'Name':'John'}
    
# @app.get('/departments/{department_id}/employees/{employee_id}')
# def info(department_id:int,employee_id:int):
#     return{department_id,employee_id}

# @app.get("/movies/{movie_id}")
# def get_movie(movie_id: int):
#     return {"movie_id": movie_id}

# @app.get("/search")
# def get_categories(query:str):
#     return{
#         'category':query
#     }
    
# @app.get('/articles')
# def get_articles(page:int, limit:int):
#     return{
#         'page':page,
#         'limit':limit
#     }
    

# @app.get("/movies")
# def get_categories(genre:str):
#     return{
#         'genre':genre
#     }
    
# @app.get('/students/{student_id}/courses')
# def get_student_data(student_id:int, semester:int):
#     return{
#         'student_id':student_id,
#         'semester':semester
#     }
    
# # /products/50 return product id 50 and discount zero,/products/50?discount=20 return product id 50 and discount 20,/products/hello?discount=20 error

class Product(BaseModel):
    name: str
    price: float

# @app.post("/products")
# def create_product(product: dict):
#     return {
#         "message": "Product created",
#         "product": product
#     }
@app.post("/products")
def create_product(product: Product):
    return product

class Book(BaseModel):
    title :str
    author :str
    pages :int
@app.post('/books')
def create_book(book:Book):
    return  book

class Student(BaseModel):
    name :str
    age :int  =Field(ge=18)
    cgpa :int
@app.post('/students')
def create_student(student:Student):
    return  student


# Request
#  ↓
# json
#  ↓
# pydantic
#  ↓
# validation
#  ↓
# function


@app.put('/books/{book_id}')
def change_data(book_id:int,book:Book):
    return {
        'book_id':book_id,
        'book':book
        
    }
@app.delete('/students/{student_id}')
def create_student(student_id:int,student:Student):
    return  {
        'student id':student_id,
        'student':student
    }
    
class employeeUpdate(BaseModel):
    name: Optional[str] = None
    department: Optional[str] = None
    salary: Optional[int] = None
@app.patch('/employees/{employee_id}')
def create_student(employee_id:int,employee:employeeUpdate):
    return  {
        'employee id':employee_id,
        'employee':employee
    }
    
# A. Get all orders get

# B. Create a new order post

# C. Change the entire order information put

# D. Change only the order's status patch

# E. Remove an order delete\\
# PATCH /users/7


books ={}
@app.get('books/:{book_id}')
def get_book(book_id:int):
    
    
    if book_id not in books:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )
    return {
        "book_id":book_id,
        "name": books[book_id]
    }
        
@app.get('/accounts/{account_id}/withdraw')
def check_amount(withdraw:float):
    if withdraw >1000:
        raise HTTPException(
            status_code=400,
            detail="Amount canot be grater than 10000"
        )
    return withdraw

