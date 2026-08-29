class Book:
    def __init__(self,book_id, title, author, is_available=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = is_available

    @property
    def book_id(self):
        return self._book_id
    @book_id.setter
    def book_id(self, value):
        if not isinstance(value, int):
            raise ValueError("Book ID must be an integer.")
        self._book_id = value
    
    @property
    def title(self):
        return self._title
    @title.setter
    def title(self,value):
        if not value or value.strip() == "":
            raise ValueError("Title cannot be empty.")
        self._title = value.strip()
    @property
    def author(self):
        return self._author
    @author.setter
    def author(self, value):
        if not value or value.strip() == "":
            raise ValueError("Author cannot be empty.")
        self._author = value.strip()
        
    def __eq__(self, other):
        if isinstance(other, Book):
            return self.book_id == other.book_id
        return False
    
    def __len__(self):
        return len(self.title)
       
    def __repr__(self):
        return f"Book(book_id={self.book_id}, title='{self.title}', author='{self.author}', is_available={self.is_available})"
    
    def __str__(self):
        return f" {self.title} by {self.author}"