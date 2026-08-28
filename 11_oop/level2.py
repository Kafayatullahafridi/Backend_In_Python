# # class Car:


# #     wheels = 4#class attri

# #     def __init__(self, brand, color):
# #         self.brand = brand#istance
# #         self.color = color#instance
        
# # class Student:

# #     university = "KUST"

# #     def __init__(self, name):
# #         self.name = name


# # s1 = Student("Ali")
# # s2 = Student("Sara")

# # print(s1.name)#ali
# # print(s2.name)#sara

# # print(s1.university)#kust
# # print(s2.university)#kust
# # class Student:

# #     university = "KUST"


# # s1 = Student()
# # s2 = Student()

# # Student.university = "FAST"

# # print(s1.university)
# # print(s2.university)#becz class attribut is same for every object
# # class Student:

# #     university = "KUST"


# # s1 = Student()
# # s2 = Student()

# # s1.university = "Harvard"

# # print(s1.university)#Harvard
# # print(s2.university)#kust 
# # print(Student.university)#kust

# class BankAccount:
#     def __init__(self,owner,balance):
#         self.owner =owner
#         self.balance = balance
        
#     def deposit(self,amount):
#        if amount>0:
#         self.balance +=amount
#        else:
#            print('Amount canot be neg')
        
#     def withdraw(self,amount):
#         if amount>=self.balance:
#             self.balance -=amount
#     def show_balance(self):
#         print(f'{self.owner} have {self.balance} in account')
        
# account = BankAccount("Ali", 1000)

# account.deposit(3500)
# account.withdraw(400)

# account.show_balance()

# class Employee:
#     company = "ABC"

#     def change_company(cls,name):
#         Employee.company = name
    
# Employee.change_company("Google")

class Calculator:
    @staticmethod
    def add(a, b):
       return a+b
print(Calculator.add(10, 20))