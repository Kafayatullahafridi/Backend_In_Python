users = [
    {"name": "Ali", "age": 25},
    {"name": "Sara", "age": 19},
    {"name": "Ahmed", "age": 22},
    {"name": "Zain", "age": 30},
]

new_list = sorted(users,key=lambda user: user["age"])
print(new_list)
descinding_order = sorted(users,key=lambda user: user["age"],reverse=True)
print(descinding_order)
