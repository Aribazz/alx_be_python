class Book:
    """A class to represent a generic book."""
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}')"


class EBook(Book):
    """A class to represent an e-book, inheriting from Book."""
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

    def __repr__(self):
        return f"EBook('{self.title}', '{self.author}', {self.file_size})"


class PrintBook(Book):
    """A class to represent a print book, inheriting from Book."""
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

    def __repr__(self):
        return f"PrintBook('{self.title}', '{self.author}', {self.page_count})"


class Library:
    """A class to represent a library that manages a collection of books."""
    def __init__(self):
        self.books = []

    def add_book(self, book):
        """Adds a book to the library's collection."""
        if isinstance(book, Book):
            self.books.append(book)
        else:
            raise ValueError("Only instances of Book or its subclasses can be added to the library.")

    def list_books(self):
        """Lists all books in the library's collection."""
        if not self.books:
            print("The library has no books.")
        else:
            for book in self.books:
                print(book)
