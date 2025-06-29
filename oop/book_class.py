"""
Book Module Demonstrating Magic Methods in Python

This module defines a simple `Book` class to illustrate the use of magic methods 
such as __init__, __str__, __repr__, and __del__. These special methods customize 
object initialization, string representation, debugging output, and object deletion behavior.
"""

class Book:
    """
    A class representing a book with a title, author, and publication year.

    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
        year (int): The year the book was published.
    """

    def __init__(self, title: str, author: str, year: int):
        """
        Initialize a new Book instance.

        Args:
            title (str): The book's title.
            author (str): The book's author.
            year (int): The year of publication.
        """
        self.title = title
        self.author = author
        self.year = year

    def __str__(self) -> str:
        """
        Return a user-friendly string representation of the Book object.

        Returns:
            str: A readable string describing the book.
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self) -> str:
        """
        Return an unambiguous string representation of the Book object,
        suitable for debugging and recreating the object.

        Returns:
            str: A string that could be used to recreate the object.
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __del__(self):
        """
        Define behavior for when a Book object is deleted.
        """
        print(f"Deleting {self.title}")
