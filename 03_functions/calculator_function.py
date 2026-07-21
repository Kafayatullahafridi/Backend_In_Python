
def add(num1,num2):
     addition = num1+num2
     print (f"Addition of {num1} and {num2} = {addition}")

def sub(num1,num2):
     subract = num1-num2
     print (f"Subtraction of {num1} and {num2} = {subract}")
def multiply(num1,num2):
     multiply = num1*num2
     print (f"Multiplication of {num1} and {num2} = {multiply}")
def division(num1,num2):
    if num2 == 0:
        print("Canot be divied by zero")
    else:    
       divide = num1/num2
       print (f"Division of {num1} and {num2} = {divide}")
    
def main():
    ADD =1
    MULTIPLY =2
    DIVIDE =3
    SUBTRACT =4
    
    print("======Menu======")
    print("1.Add\n2.Multiply\n3.Divide\n4.Subtract")
    option= int(input("Enter option from above:"))
    num1 = int(input("Enter number 1 :"))
    num2= int(input("Enter number 2 :"))
    if option ==1:
        add(num1,num2) 
    elif option==2:
        multiply(num1,num2) 
    elif option==3:
        division(num1,num2)
    elif option ==4:
        sub(num1 , num2)
    else:
        print("Invalid option") 
    
if __name__=="__main__":
    main()