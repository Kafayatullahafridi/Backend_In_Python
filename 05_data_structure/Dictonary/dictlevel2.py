# # user = {
# #     "name": "Ali",
# #     "age": 22,
# #     "email": "ali@example.com"
# # }

# # email = user.pop('email')
# # print(email)
# # phone =user.pop('phone')
# # print(phone)
# data = {
#     "a": 10,
#     "b": 20,
#     "c": 30
# }

# a,val =data.popitem()
# print(a,val)
# print(data)

# user = {
#     "name": "Ali",
#     "age": 22
# }
# user.update({    'age':23,
#     'city':'islamabad',
#     'country':'Pakistan'
# })
# print(user)
# user = {
#     "name": "Ali",
#     "age": 22
# }

# backup = user
# backup["age"] = 50

# print(user)
# print(backup)
# #becz of shallow copy and both variable are referencing to one object
# user = {
#     "name": "Ali",
#     "age": 22
# }

# backup = user.copy()
# backup["age"] = 50

# print(user)
# print(backup)
# #now they both have different objcts thats why different from q5 
# user = {
#     "name": "Ali",
#     "profile": {
#         "age": 22
#     }
# }

# backup = user.copy()

# backup["profile"]["age"] = 50

# print(user)
# print(backup)
# #the main dictonary is copied to new object but the internal ones are not copied they are still referencing to same objcts means the nested one thats why it is shallow copy
user = {
    "name": "Ali",
    "age": 22
}
user.setdefault('country','Pakistan')
print(user)
user.setdefault('age',50)
print(user)
users = {
    "ali": {
        "age": 22,
        "active": True
    },
    "ahmed": {
        "age": 25,
        "active": False
    },
    "sara": {
        "age": 21,
        "active": True
    }
}
for user,data in users.items():
    if data['active']:
        print(f'{user} is {data['age']} years old')
        

products = {
    "laptop": {"price": 80000, "stock": 5},
    "phone": {"price": 50000, "stock": 0},
    "tablet": {"price": 30000, "stock": 3},
    "monitor": {"price": 25000, "stock": 0}
}

for product , data in products.items():
    if data['price']<60000 and data['stock']>0:
        print(product)
        