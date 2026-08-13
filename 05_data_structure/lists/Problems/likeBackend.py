orders = [
    {"id": 1, "amount": 500, "status": "paid"},
    {"id": 2, "amount": 300, "status": "pending"},
    {"id": 3, "amount": 900, "status": "paid"},
    {"id": 4, "amount": 200, "status": "cancelled"},
]

total_orders =0
for order in orders:
    if order["status"] == "paid":
        total_orders += order["amount"]
print(f"The total amount of paid orders is: {total_orders}")