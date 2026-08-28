import json  # 1. Import the JSON module


DATA_FILE = "students.json"  # 2. Define the filename
Students = {}

# ------------------- JSON Helper Functions -------------------
def load_data():
    """Load student data from the JSON file. Return empty dict if file doesn't exist."""
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)  # Reads JSON and converts to Python dict
    except FileNotFoundError:
        return {}  # No file yet, start fresh

def save_data(data):
    """Save the student dictionary to the JSON file in a pretty format."""
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)  # indent=4 makes it human-readable
    print(" Data saved to file.")  # Optional feedback



def add_student(student):
  
    roll_number =(input("Enter Roll number :"))
    if roll_number not in student:
     name = input("Enter name of student:")
     major = input("Enter Major of a student:")
     cgpa = float(input("Enter CGPA :"))
     student[roll_number] ={
        'name':name,
        'major':major,
        'cgpa':cgpa
      }
    else:
       print("Student already exists")
    
    
def update(student):
    roll_number = (input("Enter Roll no to update:"))
    if roll_number in student:
     name = input("Enter name of student:")
     major = input("Enter Major of a student:")
     cgpa = float(input("Enter CGPA :"))
     student[roll_number] ={
            'name':name,
            'major':major,
            'cgpa':cgpa
        }
    else:
        print("Student Not Exists")

def delete(student):
    roll_number =(input("Enter Roll no to delete:"))
    if roll_number in student:
        del  student[roll_number]
        print("Deleted successfully!!")
    else:
        print('Student not founded')
        
def show_all(student):
    print(student)
    
def  main():
 global Students  # Allows us to assign the loaded data to the global variable

    # 3. LOAD data when the program starts
 Students = load_data()
 print(f" Loaded {len(Students)} students from '{DATA_FILE}'.")
 
 while True:
  print("========Student Managment=========")
  print("1.Add\n2.Update\n3.Delete\n4.Show all\n5.Exit")
  option =int(input("Enter option: "))
  if option==1:
     add_student(Students)
     save_data(Students)
  elif option ==2:
     update(Students)
     save_data(Students)
  elif option ==3 :
     delete(Students)
     save_data(Students)
  elif option ==4 :
     show_all(Students)
     save_data(Students)
  elif option ==6:
     break
 
main()