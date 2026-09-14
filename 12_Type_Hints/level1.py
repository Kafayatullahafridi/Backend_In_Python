name:str = "Ahmed"
age:int= 25
is_student : bool = True

def multiply(a, b)->int:
    return a * b


def get_discount(price, discount)->float:
    return price - discount

def get_name(user_id: int) -> str:# we need int but its str
    return 123