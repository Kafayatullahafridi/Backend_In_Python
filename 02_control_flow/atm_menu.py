#An ATM menu using control flow  in python
deposit =1
withdraw =2
check_balance =3
exit = 4
inital_balance  =1000
print("=======ATM MENU========")
print("1. Deposit \n2. Withdraw \n3. Check Balance \n4. Exit ")   
option = int(input("Enter option from above :"))
while option != exit:
    if (option == deposit):
        
     amount = int(input("Enter amount to deposit :"))
     if(amount==0):
         print("You cannot deposit zero ruppees")
     elif(amount<0):
         print('You cannot deposit negative rupees')
     else:
      inital_balance += amount
      print(f"Your new balance is : { inital_balance}")
    elif (option ==withdraw):
      amount = int(input("Enter amount to withdraw :"))
      if(inital_balance==0):
          print("Account balance is zero")
      elif(amount<0):
          print("Negative amount cannot be deducted")
      elif(amount ==0):
          print("Cannot withdraw 0")
      elif(amount > inital_balance):
          print("Cannot withdraw large amount than current")
      else:
      
       inital_balance = inital_balance-amount
       print(f"Your new balance is : { inital_balance}")
    elif(option==check_balance):
     print(f"Your current balance is : {inital_balance}")
    else:
     print("invalid option")
    print("=======ATM MENU========")
    print("1. Deposit \n2. Withdraw \n3. Check Balance \n4. Exit ")   
    option = int(input("Enter option from above :"))
    print("Thank you for using our ATM")