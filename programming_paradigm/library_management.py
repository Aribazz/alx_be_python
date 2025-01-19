class Book:
    """Represents a book in the library."""
    
    def __init__(self, title, author):
        """Initialize a book with a title, author, and availability status."""
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """Mark the book as checked out if it's not already checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as available."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Return whether the book is available for checkout."""
        return not self._is_checked_out


class Library:
    """Manages a collection of books in the library."""

    def __init__(self):
        """Initialize the library with an empty list of books."""
        self._books = []  # Private list to store Book instances

    def add_book(self, book):
        """Add a book to the library collection."""
        if isinstance(book, Book):
            self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title if it's available."""
        for book in self._books:
            if book.title == title and book.is_available():
                if book.check_out():
                    print(f"Checked out '{title}'.")
                    return
        print(f"'{title}' is not available or doesn't exist in the library.")

    def return_book(self, title):
        """Return a book by title."""
        for book in self._books:
            if book.title == title and not book.is_available():
                if book.return_book():
                    print(f"Returned '{title}'.")
                    return
        print(f"'{title}' is not checked out or doesn't exist in the library.")

    def list_available_books(self):
        """List all books that are currently available."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books are currently available.")