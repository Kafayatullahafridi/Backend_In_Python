# numbers = {1, 2, 2, 3, 3, 3}

# print(numbers)#{1,2,3}
# #2
# a = {}#dictonary
# b = set() #set
# c = {1, 2, 3}#set
# #3
# numbers = {1, 2, 3}

# numbers.add(2)
# numbers.add(4)

# print(numbers)#{1, 2, 3, 4}
# #4
# #remove cause an error if the element is not present in the set, discard does not cause an error if the element is not present in the set
# #5
# numbers = {1, 2, 3}

# numbers[0]#wil cause error becz set are unordered
# #6
# numbers = [1, 2, 2, 3, 4, 4, 5, 5]
# nums = set(numbers)
# print(nums)#{1, 2, 3, 4, 5}
#7
users = {"Ali", "Sara", "Ahmed"}
if 'Sara 'in users:
    print("Sara is present in the set")
 #8
 #10 valid as it is string
"Ali" #valid
(1, 2)#valid
[1, 2]#inavlid as this is list 
{"a": 1}#valid but when we have key in set it will become dictonay
#True   #valid
#10
permissions = {"read", "write", "delete"}
if 'delete' in permissions:
    print('Delete persiomm have:')
    
#10
requested_roles = ["admin", "editor", "admin", "viewer", "editor"]
unique_roles = set(requested_roles)
