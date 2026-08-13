

numbers = [9,4,8,3,99,-1,1]
max = numbers[0]
min = numbers[0]
sum =0
count=0
for num in numbers:
    sum +=num
    count+=1
    if min >num:
        min = num
    elif max<num:
        max=num



print(f"Samllest num : {min}") 
print(f"Largest num  : {max}")    
print(f'Average is   : {(sum)/count:.2f}')        