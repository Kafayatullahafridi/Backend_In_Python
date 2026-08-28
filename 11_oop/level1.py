class Car:
    def __init__(self,name):
        self.name= name
        
 
car1 = Car('Jagur')
car2 = Car('ferarri')
#car is class as a blue print , car1 and car2 are the objects

class Student:
    def __init__(self,name,age):
        self.name =name
        self.age =age
        
    def introduce(self):
       print(f'Hi my name is {self.name} and im {self.age} years old')   
student = Student("Ali", 22)
student.introduce()
print(student.name)
print(student.age)
#self refers to the name of that particulr obj
#hello ali , hello sara becz self refers to that particular obj 

