#greet is function object 
#greet() is calling func to excecute

# def greet():
#     print("Hello")

# hello = greet

# hello()#now hello and greet are same so what will in  greet will be executed 
# def square(x):
#     return x * x

# operation =square
# print(operation(5))

def execute(func):
    return func()
def say_hello():
    return "Hello"

result = execute(say_hello)

print(result)

double = lambda x:x*x
print(double(10))
numbers = [1, 2, 3, 4, 5]
square = map(lambda x:x*x,numbers)
print(list(square))
numbers = [1, 2, 3, 4, 5]
even  = filter(lambda x:x%2==0,numbers)
print(list(even))
users = [
    {"name": "Ali", "age": 25},
    {"name": "Ahmed", "age": 19},
    {"name": "Sara", "age": 30},
    {"name": "Ayesha", "age": 22}
]

names = list(map(lambda x: x['name'], filter(lambda x: x['age'] >= 21, users)))
print(list(names))