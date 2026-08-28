# def add_numbers(*args):
#     total =0
#     for num in args:
#         total+=num
#     return total

# print(add_numbers(1, 2, 3))
# print(add_numbers(10, 20, 30, 40))

# def show_names(*names):
#     for name in names:
#         print(name)

# show_names("Ali", "Ahmed", "Sara", "Ayesha")

# def test(*args):
#     print(type(args))
#     print(args)#<class 'tuple'> ,(10, 20, 30)

# test(10, 20, 30)

# def display_info(**kwargs):
#     for key , value in kwargs.items():
#         print(f'{key}:{value}')
        
# def count_arguments(*args):
#     count= 0
#     for num in args:
#         count+=1
        
#     return count
# print(count_arguments(1, 2, 3, 4, 5))

# def analyze(*args, **kwargs):
#     print(f'Positioal:{args}')
#     print(f'Keywords:{kwargs}')

# analyze(
#     10,
#     20,
#     30,
#     name="Ali",
#     age=23
# )

# numbers = [10, 20, 30]
# def add(*numbers):
#     total=0
#     for num in numbers:
#         total+=num
#     return total

# print(add(*numbers))

# user = {
#     "name": "Ali",
#     "age": 23,
#     "country": "Pakistan"
# }
# def introduce(**user):
#     for key,vals in user.items():
#         print(f'{key}:{vals}')

# introduce(**user)
def create_user(**data):
    for key,vals in data.items():
        print(f'{key}:{vals}')
user = create_user(
    username="kayfi",
    age=23,
    country="Pakistan",
    active=True
)

def test(a, *args, **kwargs):
    print(a)#10
    print(args)#(20,30)
    print(kwargs)#{'name:'Ali','age':23}

test(
    10,
    20,
    30,
    name="Ali",
    age=23
)