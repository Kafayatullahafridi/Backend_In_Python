from typing import Required,NotRequired,TypedDict

# scores:list[int] = [90, 80, 100]

# countries : list[str]= ["Pakistan", "Qatar", "Canada"]

# user_ages: dict[str,int] = {
#     "Ali": 20,
#     "Sara": 22,
#     "Ahmed": 25
# }


# def get_even_numbers(numbers:list[int])->list[int]:
#       ...
      
      
# user:tuple[str,int]= ("Ahmed", 23)

# coordinates:tuple[int,...] = (10.5, 20.7, 30.2)

# numbers:  list[list[int]] = [
#     [1, 2],
#     [3, 4],
#     [5, 6]
# ]

# employees: dict[str,list[str]] = {
#     "Engineering": ["Ali", "Sara"],
#     "Marketing": ["Ahmed", "Usman"]
# }


# def find_name(user_id: int)-> str| None:
#     if user_id == 1:
#         return "Ali"

#     return None


# def find_score(name: str) ->str|None:
#     scores = {
#         "Ali": 90,
#         "Sara": 85
#     }

#     return scores.get(name)

# def divide(a: int, b: int)->None|float:
#     if b == 0:
#         return None

#     return a / b

User = dict[str, str | int | bool]

def deactivate_user(users :list[dict[User]], user_id:int)->None:
    ...
    


def get_active_users()->list[dict[User]]:
    ...
    
def find_user(user_id)->dict[User]|None:
    ...
    
from typing import TypedDict 
    
class Product(TypedDict):
    id:int
    name:str
    price:float
    in_stock:bool
    
    
product:Product = {
    "id": 1,
    "name": "Keyboard",
    "price": 2500.0,
    "in_stock": True
}



def get_product(product_id:int)->Product|None:
   ... 


class UserUpdate(TypedDict,total=False):
    name : str
    age :int
    is_active : bool
    
class UserProfile(TypedDict):
    name : str
    age : int
    bio : str | None 
    
#in last one should use total =false


class Student(TypedDict):
    id        :int
    name      :str
    email     :str
    phone     :NotRequired[str]
    linkedin  :NotRequired[str]
    
    
class StudentUpadte(TypedDict,total=False):
    student_id :Required[int]
    name        :str
    email       :str
    phone       :str
    