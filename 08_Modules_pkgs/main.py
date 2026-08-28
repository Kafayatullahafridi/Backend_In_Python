# import calculator
# import user_utils

# # add = calculator.add(3,4)
# # print(add)

# # sub = calculator.subract(3,4)
# # print(sub)

# # mul = calculator.multiply(3,4)
# # print(mul)

# # d = calculator.divide(3,4)
# # print(d)

# user = user_utils.create_user('jon',5)
# print(user)
# print(user_utils.is_adult(550))
# # main.py



# # print(add(5, 3)) didnot use caluclator.add....


# from calculator import add,subract
# from user_utils import create_user
# print(add(4,5))
# print(subract(32,23))
# print(create_user('jon',44))
# # Explain what gets placed into your current namespace and how you access the function.
# # the first one is importing whole module the second is imporiting specific part of module
import calculator
def main():
   add = calculator.add(2,3) 
   print(add)
if __name__ =='__main__':
 main()