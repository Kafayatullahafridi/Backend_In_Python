class UserNotFound(Exception):
    pass
def find_user(users, user_id):
    if user_id not in users:
        raise UserNotFound (f'user {user_id} not found ')
    return users[user_id]

users = {
    1: "Ali",
    2: "Sara",
    3: "Ahmed"
}
print(find_user(users, 2))
