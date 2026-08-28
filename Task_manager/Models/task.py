class Task:
    
    VALID_STATUSES = {"pending", "in_progress", "completed"}

    def __init__(self,id,title,description,status):
        self.id = id
        self.title = title
        self.description = description
        self.status = status
        
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self,name):
        if not name or not name.strip():
            raise ValueError('title not entered')
        self._title=name
            
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        if value not in self.VALID_STATUSES:
            raise ValueError(f"Status must be one of {self.VALID_STATUSES}")
        self._status = value

    # ---------- Method to change status ----------
    def change_status(self, new_status):
        """Update the task status with validation."""
        self.status = new_status   # uses the setter for validation

    # ---------- String representation ----------
    def __str__(self):
        return f"Task(id={self.id}, title='{self.title}', status='{self.status}')"
    
task = Task(
    1,
    "Learn Python",
    "Finish OOP",
    'pending'
)

print(task)

task.change_status("completed")

print(task)