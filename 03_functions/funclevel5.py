# def countdown(n):
#     if n ==0:
#      return
#     print(n)
#     countdown(n-1)

# countdown(5)
# def test(n):
#     if n == 0:
#         return

#     print(n)
#     test(n - 1)

# test(4)#4321
# def count(n):
#     print(n)
#     count(n - 1)
# count(5) #it will cause recursive error as it hasnot base case
def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)
print(factorial(5))
def mystery(n):
    if n == 1:
        return 1

    return n + mystery(n - 1)

print(mystery(5))
mystery(5)
#5+10 =15
# →4+6=10
# →3+3=6
# →2+1+3
# →1=1
