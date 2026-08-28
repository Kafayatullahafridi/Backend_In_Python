a = {"Ali", "Sara", "Ahmed"}
b = {"Sara", "Zain", "Ahmed"}

result = a | b

print(result)#union will mix both and same will be disappeared
#intersection
a = {"Ali", "Sara", "Ahmed"}
b = {"Sara", "Zain", "Ahmed"}

result = a & b

print(result)#intersection will return only the common elements
a = {"Ali", "Sara", "Ahmed"}
b = {"Sara", "Zain", "Ahmed"}

print(a - b)#things in a but not in b
a = {"Ali", "Sara", "Ahmed"}
b = {"Sara", "Zain", "Ahmed"}
result = a ^ b#symmetric difference will return the elements which are not common in both sets
