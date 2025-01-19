import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    # Test for addition
    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)  # Positive integers
        self.assertEqual(self.calc.add(-1, 1), 0)  # Negative and positive
        self.assertEqual(self.calc.add(0, 0), 0)  # Zero addition
        self.assertEqual(self.calc.add(1.5, 2.5), 4.0)  # Floating-point numbers

    # Test for subtraction
    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(5, 3), 2)  # Positive integers
        self.assertEqual(self.calc.subtract(0, 5), -5)  # Subtracting from zero
        self.assertEqual(self.calc.subtract(-2, -3), 1)  # Negative integers
        self.assertEqual(self.calc.subtract(1.5, 0.5), 1.0)  # Floating-point numbers

    # Test for multiplication
    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)  # Positive integers
        self.assertEqual(self.calc.multiply(-2, 3), -6)  # Negative and positive
        self.assertEqual(self.calc.multiply(0, 5), 0)  # Multiplying by zero
        self.assertEqual(self.calc.multiply(1.5, 2.0), 3.0)  # Floating-point numbers

    # Test for division
    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(6, 3), 2.0)  # Positive integers
        self.assertEqual(self.calc.divide(-6, 3), -2.0)  # Negative and positive
        self.assertEqual(self.calc.divide(1.5, 0.5), 3.0)  # Floating-point numbers
        self.assertIsNone(self.calc.divide(5, 0))  # Division by zero

    # Test for edge cases
    def test_edge_cases(self):
        """Test edge cases for all methods."""
        self.assertEqual(self.calc.add(float('inf'), 1), float('inf'))  # Adding infinity
        self.assertEqual(self.calc.subtract(float('inf'), float('inf')), 0)  # Subtracting infinity
        self.assertEqual(self.calc.multiply(float('inf'), 0), 0)  # Multiplying infinity by zero
        self.assertIsNone(self.calc.divide(0, 0))  # Dividing zero by zero

if __name__ == "__main__":
    unittest.main()