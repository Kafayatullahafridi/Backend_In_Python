orders = [
    {"id": 1, "items": [100, 200, 50]},
    {"id": 2, "items": [300, 150]},
    {"id": 3, "items": [80, 120, 60]},
]

new_list = [
    price
    for order in orders
    for price in order["items"]
]
print(new_list)

userss = [
    {"id": 1, "name": "Ali", "age": 22, "active": True},
    {"id": 2, "name": "Sara", "age": 17, "active": True},
    {"id": 3, "name": "Ahmed", "age": 25, "active": False},
    {"id": 4, "name": "Zain", "age": 30, "active": True},
]
new_l = [
        userss['name'] for userss in userss if userss['age']>=18 and userss['active']
        
]
print(new_l)



orders = [
    {"id": 1, "amount": 500, "status": "paid"},
    {"id": 2, "amount": 300, "status": "pending"},
    {"id": 3, "amount": 900, "status": "paid"},
    {"id": 4, "amount": 200, "status": "cancelled"},
]

paid_orders = [ order for order in orders if order["status"] == "paid"]
paid_amounts = [order['amount'] for order in paid_orders]
print(paid_amounts)
paid_ids = [order['id']  for order in paid_orders ]
print(paid_ids)