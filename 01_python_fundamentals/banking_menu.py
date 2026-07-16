#A simple banking menu app in python

deposit =1
withdraw =2
check_balance =3
exit = 4
inital_balance  =1000

print("================== \n Bank Menu\n==================")
print("1. Deposit \n2. Withdraw \n3. Check Balance \n4. Exit ")
option = int(input("Enter option from above :"))
if (option == deposit):
    amount = int(input("Enter amount to deposit :"))
    inital_balance = inital_balance+amount
    print(f"Your new balance is : { inital_balance}")
elif (option ==withdraw):
    amount = int(input("Enter amount to withdraw :"))
    inital_balance = inital_balance-amount
    print(f"Your new balance is : { inital_balance}")
elif(option==check_balance):
    print(f"Your current balance is : {inital_balance}")
    
elif(option==exit):
    print("exit")
    
else:
    print("invalid option")