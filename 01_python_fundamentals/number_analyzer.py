# A number analyzer program in pyhton

number  = int(input("Enter any number to analyze :"))

if(number%2 ==0):
    print(f"{number} is even")
else:
     print(f"{number} is odd")
if(number >=0 ):
      print(f"{number} is positive")
elif (number ==0):
     print(f"{number} is zero")
else:
     print(f"{number} is negative")
if(number%2 ==0 ):
    print(f"{number} is divisible by 2")
else:
    print(f"{number} is not divisible by 2")
if(number%5 ==0 ):
      print(f"{number} is divisible by 5")
else:
    print(f"{number} is not divisible by 5")
if(number%7 ==0 ):
     print(f"{number} is divisible by 7")
else:
     print(f"{number} is not divisible by 7")
if(number%9 ==0 ):
    print(f"{number} is divisible by 9")
else:
     print(f"{number} is not divisible by 9")