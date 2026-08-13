

numbers= [1,2,2,3,3,4,4,4,5]
result=[]

for num in numbers:
    if num not in result:
        result.append(num)

print(f"List without : {result}")