# A simple program to print table for any number


number = int(input("Enter number you want to generate table of :"))
limit= int(input("Enter the number upto which you want to print:"))

for i in range(1,limit+1):
    print(f"{number} x {i} = {number*i}")
    