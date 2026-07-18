#A login system use for authentication using if/else in python

print("Welcome to our system")
name = input("Enter username:")
password= input("Enter password:")
if name == 'admin' and password == 'python123':
    print("Login Sucessful!")
    print("Welcome Admin")
elif name =='admin' and password!="python123":
    print("incorrect password")
elif name!='admin' :
    print('user name dont exists')
else:
    print("Enter valid credentails ")