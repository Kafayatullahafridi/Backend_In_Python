import csv

# with open("users.csv", "r") as f:
#     reader = csv.DictReader(f)

#     for row in reader:
#         print(row)
class filenotfound(Exception):
    pass
class userNotFound(Exception):
    pass

def load_users(filename):
    user_list= []
    with open(filename,'r')as f:
        users = csv.DictReader(f)
        for user in users:
         user['age'] = int(user['age'])
         user['id'] = int(user['id']) 
         user_list.append(user)
        return user_list
        raise  filenotfound('file not found')
users =(load_users('users.csv'))
    
def find_user(users, user_id):
    for user in users:
        if user['id'] == user_id:
            return user
    
    raise userNotFound('User not found')

print(find_user(users, 3))
def get_adults(users):
    adults=[]
    for user in users:
        if user['age']>=18:
            adults.append(user)
    return adults
    raise userNotFound('Adults users not found')
print(get_adults(users))
        