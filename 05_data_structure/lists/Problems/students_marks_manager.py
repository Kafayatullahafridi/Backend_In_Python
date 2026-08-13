


ADD_STUDENT =1
DELETE_STUDENT =2
UPDATE_STUDENT =3
SEARCH_STUDENT =4
DISPLAY_ALL_STUDENTS =5
FIND_TOPPER=6
AVERAGE_MARKS=7
HIGHEST_AND_LOWEST_MARKS =8
EXIT =9

    
    
    
def main():
    students =[]
  
    print("=======MENU=======")
    print("1.Add Studet\n2.Delete Student\n3.Update Student\n4.Search Student\n5.Display All Students\n6.Find Topper\n7.Average marks\n8.Highest and lowest \n9.Exit\n")
    option = int(input("Enter from option from above menu :"))  
    while option!=EXIT:
       
     if option==ADD_STUDENT:
          add_students(students)
          print(f"Students are : {students}")
     elif option == DELETE_STUDENT:
        print(f"Students: {students}")
        delete_student(students)
     print("=======MENU=======")
     print("1.Add Studet\n2.Delete Student\n3.Update Student\n4.Search Student\n5.Display All Students\n6.Find Topper\n7.Average marks\n8.Highest and lowest \n9.Exit\n")
     option = int(input("Enter from option from above menu :"))       
    

    
    
    
    
    

def  add_students(students):
    name =input("Enter the name of student you want to add:")
    marks = int(input("Enter marks of a student:"))
    
    student_list = [name,marks]
    students.append(student_list)
def delete_student(students):
   
    name = input("Enter Student name to delete:")
    for stu in students:
            if students[0]==name:
                del students[0]
            

main()
    

    
    