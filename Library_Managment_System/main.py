from models import Book, Member
from exeptions import BookAlreadyBorrowed, BookNotFound
from services import Library


# 1. Setup
library = Library("Campus Library")

book1 = Book(1, "Python Basics", "Alice")
book2 = Book(2, "Data Structures", "Bob")
book3 = Book(3, "Algorithms", "Charlie")

member1 = Member(101, "Sam", "sam@example.com")
member2 = Member(102, "Nia", "nia@example.com")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.add_member(member1)
library.add_member(member2)

# 2. Borrow
library.borrow_book(101, 1)
library.borrow_book(102, 2)

# 3. Generators
print("Available books:")
for book in library.available_books():
    print(f"- {book.title} (ID: {book.book_id})")

print("\nBooks borrowed by member 1:")
for book in library.member_loans(101):
    print(f"- {book.title} (ID: {book.book_id})")

# 4. Exceptions
try:
    library.borrow_book(101, 1)
except BookAlreadyBorrowed as e:
    print(f"\nException: {e}")

try:
    library.find_book(999)
except BookNotFound as e:
    print(f"\nException: {e}")

# 5. Return
library.return_book(101, 1)
print("\nAvailable books after returning book 1:")
for book in library.available_books():
    print(f"- {book.title} (ID: {book.book_id})")

# 6. Save and Load
library.save_data()

new_library = Library("Loaded Library")
new_library.load_data()

print("\nBooks loaded into new library:")
for book in new_library.books:
    print(f"- {book.book_id}: {book.title} by {book.author} | available={book.is_available}")
