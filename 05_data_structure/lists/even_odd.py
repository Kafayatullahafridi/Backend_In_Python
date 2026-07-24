
#even odd 

numbers = [9,4,8,3,99,-1,1]
def odd_even(numbers):

 for num in numbers:
    if num %2 ==0:
        print(f'Number :{num}   is even')
    else:
        print(f"Number :{num}   is odd")
        
odd_even(numbers)
        
