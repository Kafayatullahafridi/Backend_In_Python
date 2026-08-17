# # def validate_age(age):
# #     if age < 0:
# #         return 'Invalid'
# #     elif age < 18:
# #         return "Denied"
# #     else:
# #         return"Allowed"

# # print(validate_age(-5))
# # print(validate_age(15))
# # print(validate_age(25))

# # def clean_username(username):
# #     spaces_remove = username.strip().lower()
# #     remove = spaces_remove.replace('_','')
# #     if remove.isalnum():
# #         return True
# #     else:
# #         return False
    
# # print(clean_username("  Kayfi_123 "))
# users = {
#     "ali": {"age": 22, "active": True},
#     "ahmed": {"age": 17, "active": True},
#     "sara": {"age": 25, "active": False},
#     "ayesha": {"age": 20, "active": True},
#     "hamza": {"age": 16, "active": False}
# }

# def get_active_adults(users):
#     active=[]
#     for key,vals in users.items():
#         if vals['age']>=18 and vals['active'] ==True:
#             active.append(key)
#     return active
# print(get_active_adults(users))

# def calculate_total(*numbers):
#     total = 0
#     for num in numbers:
#         total+=num
#     return total

# print(calculate_total(10, 20))
# print(calculate_total(10, 20, 30, 40))
# print(calculate_total(5, 10, 15, 20, 25))

# def create_user(**data):
#     return data

# user = create_user(
#     username="kayfi",
#     age=23,
#     country="Pakistan",
#     active=True
# )
# print(create_user(**user))



# numbers = [1, 2, 3, 4, 5]
# def square(numbers):
#     squares=[]
#     for num in numbers:
#         squares.append(num*num)
#     return squares

# def apply_operation(func, numbers):
#     return func(numbers)
# print(apply_operation(square,numbers))

# products = [
#     {"name": "Laptop", "price": 80000, "stock": 5},
#     {"name": "Phone", "price": 50000, "stock": 0},
#     {"name": "Tablet", "price": 30000, "stock": 3},
#     {"name": "Monitor", "price": 25000, "stock": 0},
# ]

# def get_available_products(products):
#     prodcut =[]
#     for pro in products:
#         if pro['price']<60000 and pro['stock']>0:
#             prodcut.append(pro)
#     return prodcut
# print(get_available_products(products))

# name = "   KAYFI   "
# def clean_name(name):
#     return name.strip().lower()

# def make_username(name):
#     return name

# def add_prefix(username):
#     return 'user_'+username

# make =clean_name(name)
# addpre= make_username(make)
# print(add_prefix(addpre))


# def sum_numbers(n):
#     if n ==1:
#      return 1
#     return n + sum_numbers(n-1)
# print(sum_numbers(5))
# print(sum_numbers(10))
users = [
    {
        "username": "  KAYFI ",
        "age": 23,
        "active": True
    },
    {
        "username": " Ali ",
        "age": 17,
        "active": True
    },
    {
        "username": " SARA ",
        "age": 25,
        "active": False
    },
    {
        "username": " Ahmed ",
        "age": 30,
        "active": True
    }
]
def process_users(users):
 uss =[]
 for user in users:
    if user['age']>=18 and user['active']==True:
       cleaned_name =   user['username'].strip().lower()
       processed_users={
           'username':cleaned_name,
           'age':user['age']
       }
       uss.append(processed_users)
 return uss 
print(process_users(users)) 

def analyze_numbers(numbers):
    total =0
    average =0
    even =[]
    odd =[]
    maxi =max(numbers)
    mini =min(numbers)
    
    for num in numbers:
        total+=num
        if num%2==0:
            even.append(num)
        else:
            odd.append(num)
        average = total/len(numbers)
        analzye={
            'total':total,
            'average':average,
            'max':maxi,
            'min':mini,
            'even':even,
            'odd':odd
        }
    return analzye
numbers = [10, 15, 20, 25, 30, 35]
print(analyze_numbers(numbers))