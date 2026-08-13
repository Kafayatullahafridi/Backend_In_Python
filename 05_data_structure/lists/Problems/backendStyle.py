users = [
    {"id": 1, "name": "Ali", "age": 22, "active": True},
    {"id": 2, "name": "Sara", "age": 19, "active": False},
    {"id": 3, "name": "Ahmed", "age": 25, "active": True},
    {"id": 4, "name": "Zain", "age": 17, "active": True},
]

new_users = []
for user in users:
    if user["age"] >= 18  and user['active']:
        new_users.append(user['name'])
print(new_users)