#Students Marks Calculator 

marks  = int(input("Enter Marks from 0 - 100 "))

if(marks <=100 or marks >=90 ):
    print(f"Your marks are  : {marks}\n Grade is A+ ,Pass")
elif(marks <=89 and marks >=80):
    print(f"Your marks are  : {marks}\n Grade is A, Pass")
elif(marks <=79 and marks >=70 ):
    print(f"Your marks are  : {marks}\n Grade is B , Pass")
elif(marks <=69 and marks>=60 ):
    print(f"Your marks are  : {marks}\n Grade is C , Pass")
elif(marks <=59 and marks>=50 ):
    print(f"Your marks are  : {marks}\n Grade is D , Pass")
elif(marks <=49):
    print(f"Your marks are  : {marks}\n Grade is F ,fail ")

    
    
    