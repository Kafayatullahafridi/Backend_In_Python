try:
    number = int("20")

except ValueError:
    print("Error")

else:
    print("Success")

finally:
    print("Finished")
    
#sucess
#finished
try:
    number = int("abc")

except ValueError:
    print("Error")

else:
    print("Success")

finally:
    print("Finished")
#error 
#finised
def validate_age(age):
        if age < 0 :
            raise ValueError('Age cannot be zero or less than zero ')
        elif age>120:
            raise ValueError('Age canot be greater tha  120 yo')
        else:
            return 'Valid age'
        
def validate_age(age):
    try:
        int_age =int(age)
    except ValueError:
        print('invalid age')
    else:
        return (f'Age:{age}')            

def process_payment():
    print("Connecting to payment service")

    try:
        print("Processing payment")
        raise ConnectionError('connection is failing not conecting ')

    except ConnectionRefusedError:
        print("Payment failed")

    finally:
        print("Closing payment connection")
        
#becz through finally we will know when program will be closed 
def register_user(username, age):
    try:
        if username !=str or username =='':
            raise ValueError('Username must be string')
        elif age !=int :
            raise ValueError('age must be integer')
        elif age >13 and age <120:
            raise ValueError('age must be integer')
    except Exception:
        print(Exception)
    else:
        return username,age
    
    
        
        