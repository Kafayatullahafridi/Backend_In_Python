class UserNotFound(Exception):
    pass

class TaskNotFound(Exception):
    pass

class TaskManager:
    def __init__(self):
        self.users = []
        self.tasks = []
    def add_user(self, user):
        if any(u.id == user.id for u in self.users):
            raise ValueError("User already exists")
        self.users.append(user)

    # 2. Create a task
    def add_task(self, task):
        if any(t.id == task.id for t in self.tasks):
            raise ValueError("Task already exists")
        self.tasks.append(task)

    # 3. Find a user
    def find_user(self, user_id):
        for user in self.users:
            if user.id == user_id:
                return user
        raise UserNotFound("User not found")

    # 4. Find a task
    def find_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        raise TaskNotFound("Task not found")

    # 5. Assign a task to a user
    def assign_task(self, task_id, user_id):
        task = self.find_task(task_id)   # raises TaskNotFound if missing
        user = self.find_user(user_id)   # raises UserNotFound if missing
        user.add_task(task)

    # 6. Remove a task
    def delete_task(self, task_id):
        task = self.find_task(task_id)   # raises TaskNotFound if missing
        self.tasks.remove(task)   