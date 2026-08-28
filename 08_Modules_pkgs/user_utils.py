def create_user(name, age):
    return {
        'name':name,
        'age':age
    }
    
def is_adult(age):
    if age>=18:
        return age
    else:
        print('not an adult')