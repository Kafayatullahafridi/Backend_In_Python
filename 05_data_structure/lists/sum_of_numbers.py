

numbers = []

for num in range(5):
    num = int(input(f"Enter the number {num+1} :"))
    numbers.append(num)
print(f"Sum of  5 numbers are :{sum(numbers)}")