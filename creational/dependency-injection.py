from typing import List, Optional

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

class Library:
    def __init__(self):
        self.books = []

    def addBook(self, book: Book):
        self.books.append(book)

    def removeBook(self, isbn: str):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                return

    def listBooks(self) -> List[Book]:
        return self.books

class Reader:
    def __init__(self, library: Library):
        self.library = library
        self.checkedOutBooks = []

    def checkOutBookByISBN(self, isbn: str) -> Optional[Book]:
        for book in self.library.books:
            if book.isbn == isbn:
                self.library.removeBook(book)
                self.checkedOutBooks.append(book)
                return book
        return None

    def returnBook(self, book: Book):
        if book in self.checkedOutBooks:
            self.checkedOutBooks.remove(book)
            self.library.addBook(book)


if __name__ == "__main__":
    # Creating a library with dependency injection
    library = Library()
    book1 = Book("The Catcher in the Rye", "J.D. Salinger", "978-0-316-76948-0")
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "978-0-06-112008-4")
    library.addBook(book1)
    library.addBook(book2)

    # Creating a reader with dependency injection
    reader = Reader(library)

    # List all books in the library
    libraryBooks = library.listBooks()
    for book in libraryBooks:
        print(f"Library: {book.title} by {book.author}")

    # Check out a book
    isbnToFind = "978-0-316-76948-0"
    checkedOutBook = reader.checkOutBookByISBN(isbnToFind)
    if checkedOutBook:
        print(f"Checked out: {checkedOutBook.title} by {checkedOutBook.author}")

    # Return the book
    reader.returnBook(checkedOutBook)

    # List books in the library again
    libraryBooks = library.listBooks()
    for book in libraryBooks:
        print(f"Library: {book.title} by {book.author}")