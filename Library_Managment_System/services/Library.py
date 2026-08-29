from pathlib import Path

from data.file_handle import file_handler
from exeptions import *
from models import Book, Loan, Member
from services.notifications import EmailNotification, SMSNotification
from utils.decorators import log_action


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.members = []
        self.loans = []
        self.notifications = [EmailNotification(), SMSNotification()]
        self._next_loan_id = 1

    def _generate_loan_id(self):
        loan_id = self._next_loan_id
        self._next_loan_id += 1
        return loan_id

    @log_action
    def add_book(self, book):
        if any(existing.book_id == book.book_id for existing in self.books):
            raise ValueError(f"Book with id {book.book_id} already exists.")
        self.books.append(book)
        return book

    @log_action
    def add_member(self, member):
        if any(existing.member_id == member.member_id for existing in self.members):
            raise ValueError(f"Member with id {member.member_id} already exists.")
        self.members.append(member)
        return member

    def find_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        raise BookNotFound(f"Book with id {book_id} not found.")

    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        raise MemberNotFound(f"Member with id {member_id} not found.")

    def _send_notifications(self, message):
        for notification in self.notifications:
            notification.send(message)

    @log_action
    def borrow_book(self, member_id, book_id):
        member = self.find_member(member_id)
        book = self.find_book(book_id)

        if not book.is_available:
            raise BookAlreadyBorrowed(f"Book '{book.title}' is already borrowed.")

        member.borrow_book(book)
        book.is_available = False

        loan = Loan(self._generate_loan_id(), book, member)
        self.loans.append(loan)
        self._send_notifications(f"{member.name} borrowed '{book.title}'")
        return loan

    @log_action
    def return_book(self, member_id, book_id):
        member = self.find_member(member_id)
        book = self.find_book(book_id)

        if book.is_available:
            raise BookNotBorrowed(f"Book '{book.title}' is not currently borrowed.")

        member.return_book(book)
        book.is_available = True

        for loan in self.loans:
            if (
                loan.member.member_id == member_id
                and loan.book.book_id == book_id
                and loan.is_active
            ):
                loan.mark_as_returned()
                self._send_notifications(f"{member.name} returned '{book.title}'")
                return loan

        raise BookNotBorrowed(f"No active loan found for member {member_id} and book {book_id}.")

    def available_books(self):
        for book in self.books:
            if book.is_available:
                yield book

    def member_loans(self, member_id):
        member = self.find_member(member_id)
        for book in member.borrowed_books:
            yield book

    def save_data(self):
        base_dir = Path(__file__).resolve().parent.parent
        books_path = base_dir / "data" / "books.json"
        members_path = base_dir / "data" / "members.json"

        file_handler.save_book(self.books, str(books_path))
        file_handler.save_member(self.members, str(members_path))

    def load_data(self):
        base_dir = Path(__file__).resolve().parent.parent
        books_path = base_dir / "data" / "books.json"
        members_path = base_dir / "data" / "members.json"

        self.books = file_handler.load_books(str(books_path))
        self.members = file_handler.load_members(str(members_path))

        book_lookup = {book.book_id: book for book in self.books}
        for member in self.members:
            member.borrowed_books = [
                book_lookup[book_id]
                for book_id in getattr(member, "borrowed_books", [])
                if book_id in book_lookup
            ]
            for book in member.borrowed_books:
                book.is_available = False
