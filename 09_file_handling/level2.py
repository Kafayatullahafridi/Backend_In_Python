import json

users = {
    "1": {"name": "Ali", "age": 22},
    "2": {"name": "Sara", "age": 21}
}

with open('users.json','w')as f:
    json.dump(users,f ,indent=4)
    
    
with open("users.json", "r") as f:
    users = json.load(f)

print(users)
    
    
#idk about number 3
#dump deals with file , dumps deal with strings same is with load and loads
#5 one will dict , other will string becz in result we dumps data

# dont know abt 6

with open("users.json", "r") as f:
    users = json.load(f)


def load_users():
  ...
  
def find_user(users, user_id):
    ...
    