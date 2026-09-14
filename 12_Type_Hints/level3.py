from typing import Literal,TypedDict,Callable

status : Literal['pending','processing','completed','cancelled']

UserRole =Literal['admin','user','moderator']


def change_order_status(status: Literal['pending','processing','completed','cancelled']):
    
    ...
    
#one can accept any string the other can accept only those which are in literal list



statues =Literal['todo','inprogress','complete']
priorites =Literal['low', 'medium','high']
class Task(TypedDict):
    id:int
    name :str
    status:statues
    priority :priorites
    
def execute_operation(operation:callable[[int,int],float], a:int, b:int)->float:
    return operation(a, b)


def process_data(transformer:Callable[[list[int]],dict[str,int]], data:list[int])->dict[str,int]:
    return transformer(data)