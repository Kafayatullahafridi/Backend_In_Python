def hello():
    print('Hello , Kayfi')

hello()

def hello(name):
    print(f'Hello ,{name}')

hello('ali')

def add(a,b):
    print(a+b)
add(20,30)

def isEven(num):
    if num%2==0:
        print('even')
    else:
        print('odd')
        
isEven(5)
isEven(10)

def clean_username(name):
    new_name = name.strip().lower()
    print(new_name)
    
clean_username("   kaFRg  ")

def valid_age(age):
    if age>=18:
        print('Allowed')
    else:
        print('Not Allowed')
        
valid_age(18)