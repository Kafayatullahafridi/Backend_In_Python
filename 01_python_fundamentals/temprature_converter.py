# A simple program in pyhton which will convert temprature from fahrenheit to celsius 


option_1 = 1
option_2 = 2

user_input  = int(input("Enter one option:  \n 1. Fahrenheit to Celsius \n 2. Celsius to Fahrenheit \n:"))
temprature  = float(input("Enter temprature you wants to convert :"))

if(user_input == option_1):
    celsius =  (temprature -32)*5/9
    print(f"The temprature in Celsius is : {celsius} C")
elif(user_input ==option_2):
    fahrenheit = (temprature + 9/5)+32
    print(f"Temprature in Fahrenheit is : {fahrenheit} F")
    
else: 
    print("Invalid option , try again")
    