
# def users(filename):
#    with open(filename,'r') as f:
#         for line in f:
#          yield line.strip()

# for name in users('users.txt'):
#      print(name)
        

# def adult_users(filename):
#    with open(filename,'r') as f:
#         for line in f:
#            name,age = line.strip().split(',')
#            if int(age)>=18:
#                yield name
# for name in adult_users('users.txt'):
#      print(name)
     
     
def read_users(filename):
   with open(filename,'r') as f:
               for line in f:
                name,age = line.strip().split(',')
                user={
                   'name':name,
                   'age':int(age)
                   
                }
                yield user

users = read_users('users.txt')

def adult_users(users):
   
    for user in users:
       if user['age']>=18:
          yield user
adult = adult_users(users)
for user in adult:
     print(user)

     