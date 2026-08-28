# def decorator(func):

#     def wrapper(*args, **kwargs):
#         print("Before")

#         func(*args,**kwargs)

#         print("After")

#     return wrapper


# def greet(name):
#     print(f"Hello {name}")


# greet = decorator(greet)

# greet("Ali")

# def decorator(func):

#     def wrapper(*args, **kwargs):
#         print("Running")
#         result =func(*args, **kwargs)
#         return result  
#     return wrapper


# def add(a, b):
#     return a + b


# add = decorator(add)

# result = add(10, 20)

# print(result)

def decorator(func):

     def wrapper(*args, **kwargs):
         print("Creating user...")

         result= func(*args,**kwargs)
         return result
     return wrapper

        
         
@decorator
def create_user(name, age):
    return {
        "name": name,
        "age": age
    }

print(create_user(name="Ali", age=22))

def log(func):
   def wrapper(*args):
       print('Calling divide...')
       result = func(*args)
       return result
   return wrapper
@log
def divide(a, b):
    return a / b

result = divide(10, 2)
print(result)