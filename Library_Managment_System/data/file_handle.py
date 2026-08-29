import json
from pathlib import Path

from models.book import Book
from models.member import Member


class File_Handle:
    @staticmethod
    def _serialize_book(book):
        return {
            "book_id": book.book_id,
            "title": book.title,
            "author": book.author,
            "is_available": book.is_available,
        }

    @staticmethod
    def _serialize_member(member):
        return {
            "member_id": member.member_id,
            "name": member.name,
            "email": member.email,
            "borrowed_books": [book.book_id for book in member.borrowed_books],
        }

    def save_book(self, data, filename):
        path = Path(filename)
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8") as file:
            json.dump([self._serialize_book(item) for item in data], file, indent=4)

    def load_books(self, filename):
        path = Path(filename)
        if not path.exists():
            return []

        with path.open("r", encoding="utf-8") as file:
            loaded_books = json.load(file)

        books = []
        for book_data in loaded_books:
            books.append(
                Book(
                    book_data["book_id"],
                    book_data["title"],
                    book_data["author"],
                    book_data.get("is_available", True),
                )
            )
        return books

    def save_member(self, data, filename):
        path = Path(filename)
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8") as file:
            json.dump([self._serialize_member(item) for item in data], file, indent=4)

    def load_members(self, filename):
        path = Path(filename)
        if not path.exists():
            return []

        with path.open("r", encoding="utf-8") as file:
            loaded_members = json.load(file)

        members = []
        for member_data in loaded_members:
            member = Member(
                member_data["member_id"],
                member_data["name"],
                member_data["email"],
            )
            member.borrowed_books = member_data.get("borrowed_books", [])
            members.append(member)
        return members


file_handler = File_Handle()
