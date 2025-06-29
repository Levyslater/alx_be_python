"""
This script defines a `Calculator` class that demonstrates the use of both a class method 
and a static method to perform basic arithmetic operations.

The goal is to illustrate:
- How to use the `@staticmethod` decorator when the method doesn't need access to class or instance data.
- How to use the `@classmethod` decorator when the method needs to access or modify class-level attributes.
"""

class Calculator:
    """
    A simple calculator for demonstrating static and class methods.

    Attributes:
        calculation_type (str): A class-level attribute describing the type of calculations.
    """
    calculation_type: str = "Arithmetic Operations"

    def __init__(self):
        pass  # No instance-specific data needed for this example

    @staticmethod
    def add(a: float, b: float) -> float:
        """
        Perform addition of two numbers.

        Args:
            a (float): First number.
            b (float): Second number.

        Returns:
            float: The result of a + b.

        Note:
            This method does not access or modify any class or instance attributes.
        """
        return a + b

    @classmethod
    def multiply(cls, a: float, b: float) -> float:
        """
        Perform multiplication of two numbers and print the calculation type.

        Args:
            a (float): First number.
            b (float): Second number.

        Returns:
            float: The result of a * b.

        Note:
            This method accesses a class-level attribute (`calculation_type`).
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
