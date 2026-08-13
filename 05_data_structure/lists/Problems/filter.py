numbers = [4, 11, 7, 20, 3, 18, 9]

filtered_numbers = []
for num in numbers:
    if num > 5 and num%2==0:
        filtered_numbers.append(num)

print(filtered_numbers)