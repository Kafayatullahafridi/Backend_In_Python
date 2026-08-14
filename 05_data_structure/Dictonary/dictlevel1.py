
# student = {
#     'name':'John',
#     'age':45,
#     'departmwnt':"CS",
#     'Sem':'7th'
    
# }
# print(student)
# print(student.get('name','not provided'))
# print(student.get('email','not provided'))

# product = {
#     "name": "Laptop",
#     "price": 80000,
#     "stock": 10
# }
# product['price']= 7000
# product['brand'] ='ad'
# product['stock'] =8
# del product['brand']
# print(product)
# user = {
#     "username": "kayfi",
#     "age": 23,
#     "country": "Pakistan"
# }
# print("username" in user)#kayfi
# print("kayfi" in user)#error becz it is value
# print("email" in user)#eroor
# print("kayfi" in user.values())#True

# scores = {
#     "Ali": 85,
#     "Ahmed": 72,
#     "Sara": 91,
#     "Ayesha": 88
# }

# for key in scores.keys():
#     print(key)

# for values in scores.values():
#     print(values)
# for key,values in scores.items():
#     print(f'{key} scored {values}')

# user = {
#     "name": "Ali",
#     "profile": {
#         "age": 22,
#         "city": "Islamabad"
#     }
# }


# print(user['name'])
# print(user['profile']['age'])
# print(user['profile']['city'])
request_data = {
    "username": "kayfi",
    "email": "kayfi@example.com",
    "age": 23
}
if 'username' in request_data:
    print('yes')

print(request_data.get('username','not provided'))
print(request_data.get('phonenumber','not provided'))
request_data['is_active'] =True
print(request_data)

inventory = {
    "laptop": 5,
    "phone": 0,
    "tablet": 3,
    "monitor": 0
}
for key, value in inventory.items():
    if value >0:
        print(f'{key}:{value}')

