# A simple program to guess a number in pyhton


secret_number = 5
guess = int(input("Enter a number to guess it :"))
count=0
while guess !=5:
    count = +1
    if guess >secret_number:
        print("Too high")
    elif guess<secret_number:
        print("Too low")
    elif guess==secret_number:
        print("Congrats you guess it ")
    else:
        print("Enter valid number")
    guess = int(input("Enter a number to guess it :")) 
    
    print(f"You attempted {count} times") 