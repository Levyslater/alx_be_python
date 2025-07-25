"""
Implement a division calculator that robustly handles errors like 
division by zero and non-numeric inputs using command line arguments.
"""

def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        den = float(denominator)

        try:
            results = num / den
        except ZeroDivisionError:
            return"Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
    else:
        return f"The result of the division is {results}"