# # # class TaskManager:

# # #     def __init__(self):
# # #         self.tasks = []

# # #     def add_task(self, task:list)->list:
# # #         self.tasks.append(task)

# # #     def find_task(self, task_id:int)->None:
# # #         for task in self.tasks:
# # #             if task["id"] == task_id:
# # #                 return task

# # #         return None

# # #     def update_status(self, task_id:int, status:str)->bool:
# # #         task = self.find_task(task_id)

# # #         if task is None:
# # #             return False

# # #         task["status"] = status
# # #         return True

# # #     def get_tasks_by_status(self, status:str)->list:
# # #         return [
# # #             task
# # #             for task in self.tasks
# # #             if task["status"] == status
# # #         ]

# # #     def apply_to_tasks(self, operation:list )->list:
# # #         results = []

# # #         for task in self.tasks:
# # #             results.append(operation(task))

# # #         return results
    
    
    
# # # class UserManager:

# # #     def __init__(self)->list:
# # #         self.users = []

# # #     def add_user(self, user:dict[])->list[dict[]]:
# # #         self.users.append(user)

# # #     def find_user(self, user_id:int)->dict[]:
# # #         for user in self.users:
# # #             if user["id"] == user_id:
# # #                 return user

# # #         return None

# # class Productlist(TypedDict):
# #         id:int
# #         name:str
# #         quantity:int
# #         instock:bool

# # class ProductManager:
   

# #     def __init__(self)->None:
# #         self.products:list[Productlist] = []

# #     def add_product(self, product:Productlist)->None:
# #         self.products.append(product)

# #     def find_product(self, product_id:int)->Optional[Productlist]:
# #            for product in self.products:
# #             if product["id"] == product_id:
# #                 return product

# #            return None

# #     def update_stock(self, product_id:int, in_stock:bool)->Bool:
# #         product = self.find_product(product_id)

# #         if product is None:
# #             return False

# #         product["in_stock"] = in_stock
# #         return True
    
    
# statuses = Literal['pending','processing','shipped','delivered','cancelled']  
# class order(TypeDict):
#     id:int
#     quantity:int
#     status:statuses
      

# class OrderManager:

#     def __init__(self):
#         self.orders:list[order] = []

#     def add_order(self, order:order)->None:
#         self.orders.append(order)

#     def change_status(self, order_id:int, status:str)->bool:
#         for order in self.orders:
#             if order["id"] == order_id:
#                 order["status"] = status
#                 return True

#         return False

#     def get_orders_by_status(self, status:str)->order:
#         return [
#             order
#             for order in self.orders
#             if order["status"] == status
#         ]
        
        
        
# class NumberProcessor:

#     def process(self, numbers:list[int], operation:Callable[[int]],int)->list[int]:
#         results = []

#         for number in numbers:
#             results.append(operation(number))

#         return results
  
# class DataProcessor:
        
#     dataType = TypeVar(T)
#     def process(self, data:dataType, transformer:list[T])->list[T]:
#         results:list[T] = []

#         for item in data:
#             result = transformer(item)
#             results.append(result)

#         return results
    
    
# class user(TypedDict,total=None):
#     id        :int
#     name      : str
#     email     : str
#     age       : int
#     is_active : bool
    
# class UserManager:

#     def __init__(self)->None:
#         self.users:list[user] = []

#     def add_user(self, user:user)->None:
#         self.users.append(user)

#     def update_user(self, user_id:int, updates:user)->user|None:
#         for user in self.users:
#             if user["id"] == user_id:

#                 for key, value in updates.items():
#                     user[key] = value

#                 return user

#         return None
    
class DataFormatter:

    def format_data(self, values:list[object])->list[object]:
        formatted:list[object] = []

        for value in values:

            if isinstance(value, str):
                formatted.append(value.upper())

            elif isinstance(value, bool):
                formatted.append("YES" if value else "NO")

            elif isinstance(value, int):
                formatted.append(value * 10)

            else:
                formatted.append(value)

        return formatted