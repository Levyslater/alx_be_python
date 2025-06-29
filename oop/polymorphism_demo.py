"""
This script demonstrates the use of inheritance and method overriding in Python.

It defines a base class `Shape` with an abstract `area()` method and two derived classes:
- `Rectangle`, which calculates area as length × width.
- `Circle`, which calculates area using the formula π × r².

Each subclass overrides the base class's `area()` method to provide its specific implementation.
"""

import math


class Shape:
    """
    Base class for geometric shapes.

    Methods:
        area(): Raises NotImplementedError. Must be overridden by subclasses.
    """
    def __init__(self):
        pass

    def area(self):
        """
        Compute the area of the shape.

        Raises:
            NotImplementedError: Indicates that this method should be implemented by a subclass.
        """
        raise NotImplementedError("Derived classes need to override this method")


class Rectangle(Shape):
    """
    A rectangle shape defined by its length and width.

    Attributes:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Methods:
        area(): Returns the area of the rectangle.
    """
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns:
            float: The area of the rectangle (length × width).
        """
        return self.length * self.width


class Circle(Shape):
    """
    A circle shape defined by its radius.

    Attributes:
        radius (float): The radius of the circle.

    Methods:
        area(): Returns the area of the circle.
    """
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def area(self):
        """
        Calculate and return the area of the circle.

        Returns:
            float: The area of the circle (π × radius²).
        """
        return math.pi * (self.radius ** 2)
