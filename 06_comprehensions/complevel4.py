numbers = [1, 2, 3, 4, 5]
squares = {number:number*number for number in numbers}
print(squares)
prices = {
    "laptop": 1000,
    "mouse": 50,
    "keyboard": 80
}
doubled ={prodcut:price*2 for prodcut , price in prices.items()}
print(doubled)
prices = {
    "laptop": 1000,
    "mouse": 50,
    "keyboard": 80,
    "monitor": 300
}
below = {product:price for product,price in prices.items() if price<100}
print(below)

scores = {
    "Ali": 85,
    "Sara": 42,
    "Ahmad": 70,
    "Zain": 35
}
pass_fail = {name: 'pass' if marks >50 else 'fail' for name,marks in scores.items()}
print(pass_fail)

products = [
    {"id": 101, "name": "Laptop", "price": 1200},
    {"id": 102, "name": "Mouse", "price": 50},
    {"id": 103, "name": "Keyboard", "price": 80},
    {"id": 104, "name": "Monitor", "price": 300}
]
cheaper = {user['id']:user['name'] for user in products if user['price']<100}
print(cheaper)
users = [
    {"username": "Ali", "active": True},
    {"username": "Sara", "active": False},
    {"username": "Ahmad", "active": True}
]

status = {user['username'].lower():'active' if user['active']==True else 'inactive' for user in users}
print(status)
inventory = {
    "laptop": 10,
    "mouse": 0,
    "keyboard": 5,
    "monitor": 0,
    "webcam": 8
}
availibility = { name:'available' for name,value in inventory.items() if value>0}
print(availibility)