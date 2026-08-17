numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
flatten = [number for row in numbers for number in row]
print(flatten)

numbers = [
    [1, 2],
    [3, 4],
    [5, 6]
]
squares = [num*num for row in numbers for num in row]
print(squares)
numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
even= [num for row in numbers for num in row if num%2==0]
print(even)
numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# Input:list
# Outer item:row
# Inner item:elemnt in row
# Condition:num>4
# Transformation:if num>4 then num*num
# Output:list of nums sqaure who are grter than 4
squares = [num*num  for row in numbers for num in row if num>4]
print(squares)
users = [
    {
        "username": "Ali",
        "roles": ["admin", "user"]
    },
    {
        "username": "Sara",
        "roles": ["user"]
    },
    {
        "username": "Ahmad",
        "roles": ["admin", "editor"]
    }
]
rolss = [role for user in users for role in user['roles']]
print(rolss)
admin = [role for user in users for role in user['roles'] if role =='admin']
print(admin)
orders = [
    {
        "id": 1,
        "items": [
            {"name": "Laptop", "price": 1000},
            {"name": "Mouse", "price": 50}
        ]
    },
    {
        "id": 2,
        "items": [
            {"name": "Keyboard", "price": 80},
            {"name": "Monitor", "price": 300}
        ]
    }
]

# Input:nested list 
# Outer item:data about product
# Inner item:name and price of item
# Condition:price<100
# Transformation:flaten list
# Output:item names whose price<100
price = [item['name'] for prodcut in orders for item in prodcut['items'] if item['price']<100 ]
print(price)

students = [
    {
        "name": "Ali",
        "scores": [80, 90, 70]
    },
    {
        "name": "Sara",
        "scores": [95, 85, 100]
    },
    {
        "name": "Ahmad",
        "scores": [60, 75, 80]
    }
]
scores = [score for student in students for score in student['scores'] if score>=80 ]
print(scores)