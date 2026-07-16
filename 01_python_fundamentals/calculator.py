# A simple calculator using python



first_number = int(input("Enter first number :"))
operator     = (input("Enter operator from: + , - , / , // , % , * :"))
Second_number = int(input("Enter second number :"))

if(operator == "+"):
    Sum  = first_number + Second_number
    print(f"Sum of Numbers is : {Sum}")
elif (operator == "-"):
     Subract = first_number - Second_number
     print(f"Difference of Numbers is : {Subract}")
elif (operator == "*"):
     product  = first_number * Second_number
     print(f"Product of Numbers is : {product}")
elif (operator == "/"):
     if(Second_number == 0):
         print("Division by zero is not allowed")
     else:
      divison = first_number / Second_number
      print(f"Division of Numbers is : {divison}")
elif (operator == "//"):
     if(Second_number == 0):
         print("Division by zero is not allowed")
     else:
      floor_division  = first_number // Second_number
      print(f"floor division of Numbers is : {floor_division}")
elif (operator == "%"):
     if(Second_number == 0):
         print("Division by zero is not allowed")
     else:
      modulus  = first_number % Second_number
      print(f"Modulus of Numbers is : {modulus}") 

else:
    print("Invalid operator")
