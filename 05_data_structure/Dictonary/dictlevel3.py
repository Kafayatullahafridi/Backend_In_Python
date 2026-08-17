# user = {
#     "username": "kayfi",
#     "age": 23,
#     "active": True
# }

# if 'username' in user and user['age'] >18 and user['active'] == True :
#     print("valid user")
# else:
#     print("Invalid user")

# user = {
#     "username": "kayfi",
#     "age": 23
# }
# print(f'UserName:{user['username']}\nAge: {user['age']}\nEmail:{ user.get('email','not provided')}')

users = {
    "ali": {"age": 22, "active": True},
    "ahmed": {"age": 17, "active": True},
    "sara": {"age": 25, "active": False},
    "ayesha": {"age": 20, "active": True},
    "hamza": {"age": 16, "active": False}
}

for user , data in users.items():
    if data['age']>18 and data['active'] ==True:
        print(user)
        
scores = {
    "Ali": 85,
    "Ahmed": 92,
    "Sara": 78,
    "Ayesha": 95,
    "Hamza": 88
}
high =0
name =None
for key,value in scores.items():
   
    if  value >high:
        high =value
        name= key
        
        
print(f'{key} scored {high}')