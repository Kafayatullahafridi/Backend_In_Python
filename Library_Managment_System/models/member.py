
class Member:
    def __init__(self, member_id, name, email):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.borrowed_books = []
    
    @property
    def member_id(self):
        return self._member_id  
    
    @member_id.setter
    def member_id(self, value):
        if not isinstance(value, int):
            raise ValueError("Member ID must be an integer.")
        self._member_id = value 
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value or value.strip() == "":
            raise ValueError("Name cannot be empty.")
        self._name = value.strip()

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
      if "@" not in value or "." not in value:
            raise ValueError("Invalid email address.")
      self._email = value.strip()
      
    def borrow_book(self, book):
            self.borrowed_books.append(book)        
    def return_book(self, book):
            self.borrowed_books.remove(book)
    
    def __repr__(self):
        return f"Member(member_id={self.member_id}, name='{self.name}', email='{self.email}')"
    def __str__(self):
        return f"{self.name} ({self.email})"
    
    def __len__(self):
        return len(self.borrowed_books)
    