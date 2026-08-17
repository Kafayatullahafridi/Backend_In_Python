# numbers = [2, 4, 6, 8, 10]

# # result = []

# # for number in numbers:
# #     result.append(number * 3)
    
# #comprehension version
# result =[number*3 for number in numbers]
# print(result)

# names = ["ali", "sara", "ahmad", "zain"]
# upper =[name.upper() for name in names]
# print(upper)
# numbers = [3, 8, 11, 14, 17, 20, 23, 26]
# greater = [number for number in numbers if number>15]
# print(greater)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# even_square = [number*number for number in numbers if number%2==0]
# print(even_square)
# users = [
#     {"username": "Ali", "active": True},
#     {"username": "Sara", "active": False},
#     {"username": "Ahmad", "active": True},
#     {"username": "Zain", "active": False},
# ]
# active = [user['username'].upper() for user in users if user['active']==True]
# print(active) 
# numbers = [4, 11, 7, 15, 20, 3]
# double = [num+num for num in numbers if num >10]
# print(double)
# #a==comprehension
# #b===loop
# #c ===compre
# #d===loop
# prices = [50, 120, 75, 200, 99, 150, 30]
# below = [num for num in numbers if num <100]
# print(below)
numbers = [5, 12, 7, 20, 3, 18, 25]
# Input:numbers list
# Condition:number>10
# Transformation:number*2
# Output:list of numbers with double values which are greater than 10
greater = [number for number in numbers if number>10]
print(greater)
users = [
    {"name": "Ali", "age": 17},
    {"name": "Sara", "age": 22},
    {"name": "Ahmad", "age": 15},
    {"name": "Zain", "age": 25},
]

age = [user['name'].lower() for user in users if user['age'] >=18]
print(age)
words = ["python", "api", "backend", "sql", "fastapi"]
length = [word for word in words if len(word)>3]
print(length)
products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Mouse", "price": 40},
    {"name": "Keyboard", "price": 80},
    {"name": "Monitor", "price": 300},
]

prodcut_names = [product['name'].lower() for product in products if product['price']<100 ]
print(prodcut_names)