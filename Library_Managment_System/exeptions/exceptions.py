class LibraryException(Exception):
    """Base class for all library-related exceptions."""
    pass

class BookNotFound(LibraryException):
    """Raised when a requested book is not found in the library."""
    pass
class MemberNotFound(LibraryException):
    """Raised when a requested member is not found in the library."""
    pass

class BookAlreadyBorrowed(LibraryException):
    """Raised when a requested book is already borrowed."""
    pass
class BookNotBorrowed(LibraryException):
    """Raised when a requested book is not borrowed."""
    pass