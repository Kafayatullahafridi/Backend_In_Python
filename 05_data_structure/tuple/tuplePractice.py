# a = (10)#int 
# b = (10,)#tuple
# c = ()#tuple
# d = (10, 20)#tuple
# #2
# numbers = (1, 2, 3)

# numbers[0] = 100 #typeerror becz tuple are immuatable
# #3
# user = ("Ali", 22, True)

# name, age, active = user

# print(name)#"Ali"
# print(age)#22
# print(active)#True 
# #4
# numbers = (1, 2, 3, 4, 5)

# first, *middle, last = numbers#first =1,middle=[2,3,4],last=5
# #5
# def get_user():
#     return "Ali", 23
# name, age = get_user()
# #name will be Ali and age will be 23
# #6
# user = ("Ali", 22, "Pakistan")

# name, age,country = user
#7
users = [
    ("Ali", 22),
    ("Sara", 19),
    ("Ahmed", 25)
]
for index, (name, age) in enumerate(users):
    print(f" {name} is  {age}")
#8
a = 100
b = 200
a,b =b,a
print(a,b)
#9
data = ([1, 2], [3, 4])

data[0].append(99)

print(data)# ([1, 2,99], [3, 4])
#10
user_record = (42, "Ali", "ali@example.com", True)
user_id,name,email,is_active = user_record
print(f'User ID: {user_id}, Name: {name}, Email: {email}, Active: {is_active}')