from pydantic import BaseModel,Field


# class Student(BaseModel):
#    name       : str
#    age        : int
#    cgpa       : float
#    is_active  : bool

# student = Student(
#     name="Kayfi",
#     age="23",
#     cgpa="3.91",
#     is_active=True
# )
# print(student)
# print(student)
# print(type(student.age))
# print(type(student.cgpa))
# Student(
#     name="Kayfi",
#     age="hello",
#     cgpa=3.91,
#     is_active=True
# )
#age is hello but we want it in int and in pydantic we must have that datatype
# class Product(BaseModel):
#     name       : str
#     price      :float
#     in_stock   :bool=True
#     quantity    :int=  0
#     category   : str="General"
#     discount   : float | None =None
    
# product1 =Product(name='jon',price=23.4,in_stock=True,quantity=12,discount=232.0)
# product2 = Product(name='fds',price=12.2)
# print(product1)
# print(product2)


# class Product(BaseModel):
#     name:str =Field(min_length=3)
#     price:float =Field(gt=0)
#     quantity:float =0 ,Field(ge=0)
#     category:str='general',Field(min_length=3)
    
# p1= Product(name="Laptop", price=1000)
# print(p1)


# class Address(BaseModel):
#     city       :str
#     country    : str
#     postal_code : int
# class User(BaseModel):  
#    username : str
#    email    : str
#    address  : Address
# User(username= 'Kayfi',
# email= 'kayfi@example.com'
# ,
# address=Address(
#     city= 'Kohat',
#     country= 'Pakistan',
#     postal_code= 26000)
# )


class Product(BaseModel):
    name  : str
    price : float
    
class Order(BaseModel):
    order_id : int
    items    : list[Product]
    
order = Order(
    order_id=1,
    items=[
        {
            "name": "Laptop",
            "price": 1000
        },
        {
            "name": "Mouse",
            "price": 25
        },
        {
            "name": "Keyboard",
            "price": 50
        }
    ]
)
# print(order)
# print(type(order.items))
# print(type(order.items[0]))
# print(order.items[0].name)
# print(order.items[1].price)
# order_id=1 items=[Product(name='Laptop', price=1000.0), Product(name='Mouse', price=25.0), Product(name='Keyboard', price=50.0)]
# <class 'list'>
# <class '__main__.Product'>
# Laptop
# 25.0
# (.venv) PS C:\Use

data = order.model_dump()
print(data)
print(type(data))
print(type(data["items"]))
print(type(data["items"][0]))
product = Product(
    name="Keyboard",
    price=50
)

data = product.model_dump()

data["price"] = 40

print(data)
print(product)
print(type(data))
print(type(product))