# 10 #yes 
# "hello"#yes
# (1, 2)#yes
# (1, [2, 3])#no
# [1, 2]#no
# {"a": 1}#yes
# True#yes
# frozenset({1, 2})#yes
# numbers = [1, 2, 3, 2, 4, 5, 3]

# print(len(numbers))#6
# print(len(set(numbers)))#5
# def has_duplicates(items):
#     return len(items) != len(set(items))

# numbers = [5, 2, 8, 3, 2, 9, 8]
# duplicates = set()
# for number in numbers:
#     if number in duplicates:
#         print(f"Duplicate found: {number}")
#     else:
#         duplicates.add(number)
# user_ids = [101, 102, 103, 101, 104]
# duplicate_ids = set()
# for user_id in user_ids:
#     if user_id in duplicate_ids:
#         print(f"Duplicate user ID found: {user_id}")
#     else:
#         duplicate_ids.add(user_id)

# A : list
# b:set
# c:list
# d:set
# e:set

# set becz set are hashable and list are unhashable

requested_permissions = {
    "read",
    "write",
    "delete",
    "export"
}

allowed_permissions = {
    "read",
    "write"
}

denied = requested_permissions - allowed_permissions
granted = requested_permissions & allowed_permissions
print(denied,granted)