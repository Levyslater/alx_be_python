"""
unittest for a simple calculator module
"""
import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), self.calc.add(3, 2))
        self.assertAlmostEqual(self.calc.add(1.2, 3.4), 4.6)
        self.assertEqual(self.calc.add(-1, -1), -2)
    
    def test_subtraction(self):
        """Test for the subtraction method"""
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertNotEqual(self.calc.subtract(0, -1), self.calc.subtract(-1, 0))
        self.assertEqual(self.calc.subtract(-1, -1), 0)
    def test_multiplication(self):
        """Test for the multiplication method"""
        self.assertEqual(self.calc.multiply(0, 0), 0)
        self.assertEqual(self.calc.multiply(0, -1), 0)
        self.assertEqual(self.calc.multiply(-1, -1), 1)
    def test_division(self):
        """Test for the division method"""
        self.assertIsNone(self.calc.divide(0, 0))
        self.assertAlmostEqual(self.calc.divide(5, 2), 2.5)
        self.assertEqual(self.calc.divide(-1, -1), 1.0)