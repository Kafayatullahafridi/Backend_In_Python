# numbers = [1, 2, 3, 4, 5, 6]
# new_list = [ 'even' if number %2==0 else 'odd' for number in numbers] 
# print(new_list)

# numbers = [2, 5, 8, 11, 14]
# new_list = [num*2 if num%2==0 else num*3 for num in numbers]
# print(new_list)
# ages = [12, 18, 25, 15, 30, 10]
# age =[age for age in ages if age>=18]
# print(age)
# age_list = ['adult' if age>=18 else 'minor' for age in ages]
# print(age_list)
# names = ["Ali", "sara", "AHMAD", "zain"]
# name_list = ['clean' if name ==name.lower() else 'needs cleaning' for name in names]
# print(name_list)
users = [
    {"username": "Ali", "active": True},
    {"username": "Sara", "active": False},
    {"username": "Ahmad", "active": True},
    {"username": "Zain", "active": False},
]
names_list = [ user['username'].lower() + ':active' if user['active']==True else user['username'].lower()+ ':inactive'for user in users]

print(names_list)
# Input:list of numbers
# Item:a single number
# Condition:number*2,number*3
# If true:number*2
# If false:number*3
# Output:list of numbers multiply by 3 or 2 depends in condition
numbers = [2, 5, 8, 11, 14]
numbers_list = [num*2 if num>10 else num*3 for num in numbers]
print(numbers_list)
A = [x for x in numbers if x > 5]#this one is filtering numbers if they are greater than 5
B = ["big" if x > 5 else "small" for x in numbers]#here we are filtering but the len of list will remain same as we are not leaving any becz we are dooing if else and assinging status to each
products = [
    {"name": "Laptop", "stock": 10},
    {"name": "Mouse", "stock": 0},
    {"name": "Keyboard", "stock": 5},
    {"name": "Monitor", "stock": 0},
]
product_list  = [ product['name'].lower()+':available' if product['stock']>0 else product['name'].lower()+':out_of_stock' for product in products]
print(product_list)