

# try:
#    age =int(input('Enter your age'))
#    print(f'You are {age} years old ')
# except :
#     print('Invalid age')
    
# numbers = [10, 20, 30, 40]
# try: 
#     index =int(input('Enter the index u wanna access'))
#     print(numbers[index])
# except ValueError:
#     print("Please enter a valid number.")
# except IndexError:
#     print('index doesnot exists') 

user = {
    "name": "Ali",
    "age": 21,
    "role": "developer"
}

try:
    key =input('Enter key to access value ')
    print(user[key])
except KeyError:
    print('field doesnot exists')
 
def get_user_age(user):
    try:
       return user["age"]
    except ValueError:
        print('value not find')

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print('number canot be divied by zero')
        
    