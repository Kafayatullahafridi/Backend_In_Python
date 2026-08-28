numbers = [3, 5, 7, 9, 12]
new_list = any(number%2==0 for number in numbers)
print(new_list)

numbers = [10, 20, 30, 40]
new_L = all(number%2==0 for number in numbers)
print(new_L)


