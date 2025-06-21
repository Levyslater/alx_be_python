""" a simple book manager """

class Book:
    """ This class initializes a book through attributes like title and author """
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Checks if a book is available and checks it out making it
        unavailable"""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Checks if a book was checked out and marks it as available """
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """ Checks is a book is available and returns True, False otherwise"""
        return not self._is_checked_out

    def __str__(self):
        """ returns a humanized reprensentation of the class """
        return f'{self.title} by {self.author}'

class Library:
    """This class manages the Book instances by storing them in a list"""
    def __init__(self):
        """Initializes an empty list to store Book instances"""
        self._book = []

    def add_book(self, book):
        """Adds book instances to the list"""
        self._book.append(book)

    def check_out_book(self, title):
        """ marks a book as checked out, making it unavailable untill it's 
        returned"""
        for book in self._book:
            if book.title == title and book.is_available():
                book.check_out()
                return f'Checked out: {book}'
        return "Book not available for checkout."

    def return_book(self, title):
        """If a book was previously checked out, the book is unchecked
        and made available """
        for book in self._book:
            if book.title == title and not book.is_available():
                book.return_book()
                return f'Returned: {book}'
        return "Book not found or already returned."

    def list_available_books(self):
        """ iterates through the list and prints a string representation on instances
        that are available seoerated bya new line"""
        available = [str(book) for book in self._book if book.is_available()]
        if not available:
            print("No books available.")
        print("\n".join(available))
