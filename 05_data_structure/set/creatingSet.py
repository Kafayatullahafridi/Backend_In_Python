numbers = {1, 2, 3, 4}
names = {"Ali", "Sara", "Ahmed"}
print(numbers)
numbers = {1, 2, 2, 3, 3, 3}

print(numbers)
empty = {}#empty set is dictonary
print(type(empty))
empty = set()
print(type(empty))
#set are unordered
numbers = [10, 20, 30]

numbers[0]#will cause errror
numbers.update({8, 9})
numbers.discard(3)
numbers.discard(99)