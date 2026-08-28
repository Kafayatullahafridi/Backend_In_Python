
# with open('notes.txt','r') as f:
#    print(f.readlines())
with open('student.txt','w') as f:
    f.write("Name: Ali \nAge: 22\nCourse: Computer Science")
    
with open('student.txt','a') as f:
    f.write('\nUniversity: KUST')
    
#append added text at last where as write rewrite new like if open doc in w mode the old text will fade
def load_users(file):
    with open(file,'r') as f:
      try:
       return f.readlines()
      except FileNotFoundError:
          return 'no file exists'
print(load_users('users.txt'))       
# def load_data():
#     file = open("data.txt", "r")
    
#     try:
#         return file.read()
#     except FileNotFoundError:
#         return "No file" it is not closed as we didnot use with method so closing is importatn here

def load_users(file):
   try: 
     with open(file, 'r') as f:
        return f.readlines()
   except FileNotFoundError:
            return 'no file exists'