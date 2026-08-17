def add(a,b):
    return a+b

result = add(10, 20)
print(result)

def square(num):
    return num*num
result = square(7)
print(result)

def test():
    print("Hello")
    
result = test()

print(result)#none becz it has already print

def is_even(number):
    if number%2==0:
        return True
    return False
print(is_even(10))
print(is_even(7))
def is_adult(age):
    if age>=18:
        return True
    return False

if is_adult(23):
    print("Access granted")
else:
    print("Access denied")
    
def clean_username(name):
    new_name = name.strip().lower()
    return new_name
result = clean_username("   KAYFI   ")
print(result)

def get_user():
    return 'ali',23,'cs'
name, age, department = get_user()
print(name,age,department)

def validate_age(age):
    if 0>age:
        return 'invalid'
    elif age<18:
        return 'denied'
    return 'Allowed'
print(validate_age(-5))
print(validate_age(15))
print(validate_age(25))

def validate_username(username):
    new_name = username.strip().lower()
    remove = new_name.replace('_','')
    if len(remove)>=3 and remove.alpnum:
        return True
    
if validate_username("  Kayfi_123 "):
    print("Username accepted")
else:
    print("Username rejected")