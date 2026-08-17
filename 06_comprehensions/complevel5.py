numbers = [1, 2, 2, 3, 4, 4, 5]
unique = {num for num in numbers}
print(unique)
numbers = [1, 2, 3, 4, 5]
squares = {num*num for num in numbers}
print(squares)
numbers = [3, 8, 11, 14, 17, 20, 23, 26]
grter = {num for num in numbers if num >15}
print(grter)
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even ={num*num for num in numbers if num %2==0}
print(even)
users = [
    {"username": "Ali"},
    {"username": "Sara"},
    {"username": "Ali"},
    {"username": "Ahmad"},
    {"username": "Sara"}
]
unique = {user['username'] for user in users}
print(unique)
users = [
    {
        "name": "Ali",
        "roles": ["admin", "user"]
    },
    {
        "name": "Sara",
        "roles": ["user", "editor"]
    },
    {
        "name": "Ahmad",
        "roles": ["admin", "editor"]
    }
]
roles = {role for user in users for role in user['roles'] }
print(roles)
products = [
    {"name": "Laptop", "tags": ["Electronics", "Premium", "Computer"]},
    {"name": "Mouse", "tags": ["Electronics", "Accessory"]},
    {"name": "Keyboard", "tags": ["Computer", "Accessory"]},
]

length = {tag.lower() for prodcut in products for tag in prodcut['tags'] if len(tag)>6}
print(length)
users = [
    {
        "name": "Ali",
        "active": True,
        "skills": ["Python", "SQL", "Git"]
    },
    {
        "name": "Sara",
        "active": False,
        "skills": ["Python", "React"]
    },
    {
        "name": "Ahmad",
        "active": True,
        "skills": ["Python", "FastAPI"]
    }
]
skills = {skill.lower() for user in users for skill in user['skills'] if user['active']==True}
print(skills)
# 9.1 list compre becz in set e havenot indexs
orders = [
    {
        "id": 1,
        "items": [
            {"name": "Laptop", "category": "Electronics"},
            {"name": "Mouse", "category": "Accessories"},
        ]
    },
    {
        "id": 2,
        "items": [
            {"name": "Keyboard", "category": "Accessories"},
            {"name": "Monitor", "category": "Electronics"},
        ]
    }
]
category = {cate['category'].lower() for prodcut in orders for cate in prodcut['items']}
print(category)