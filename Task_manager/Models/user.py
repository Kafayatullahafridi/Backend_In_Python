class User:
    def __init__(self, id, name, email):
        self.id = id                
        self.name = name            
        self.email = email          
        self.tasks = []             

    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value or not value.strip():
            raise ValueError("Name cannot be empty")
        self._name = value.strip()

    
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if "@" not in value:
            raise ValueError("Email must contain '@'")
        self._email = value

    
    def add_task(self, task):
        """Add a task to the user's task list."""
        self.tasks.append(task)

    def remove_task(self, task):
        """Remove a task from the user's task list. Raises ValueError if not found."""
        if task not in self.tasks:
            raise ValueError(f"Task '{task}' not found in user's tasks")
        self.tasks.remove(task)

    def get_tasks(self):
        """Return the list of tasks assigned to the user."""
        return self.tasks


    def __str__(self):
        return f"User(id={self.id}, name='{self.name}', email='{self.email}', tasks={len(self.tasks)})"