import unittest
from Code13Correct.py import fibonacci, factorial  

class TestMathFunctions(unittest.TestCase):

    # Tests for Fibonacci function
    def test_fibonacci_negative(self):
        """Test if fibonacci function handles negative inputs"""
        result = fibonacci(-1)
        self.assertEqual(result, "Input must be a non-negative integer.")

    def test_fibonacci_zero(self):
        """Test if fibonacci(0) returns 0"""
        result = fibonacci(0)
        self.assertEqual(result, 0)

    def test_fibonacci_one(self):
        """Test if fibonacci(1) returns 1"""
        result = fibonacci(1)
        self.assertEqual(result, 1)

    def test_fibonacci_positive(self):
        """Test if fibonacci function correctly calculates the fibonacci sequence"""
        test_cases = {
            2: 1,
            3: 2,
            4: 3,
            5: 5,
            6: 8,
            7: 13,
            8: 21,
            9: 34
        }
        for n, expected in test_cases.items():
            result = fibonacci(n)
            self.assertEqual(result, expected)

    # Tests for Factorial function
    def test_factorial_negative(self):
        """Test if factorial function handles negative inputs"""
        result = factorial(-1)
        self.assertEqual(result, "Input must be a non-negative integer.")

    def test_factorial_zero(self):
        """Test if factorial(0) returns 1"""
        result = factorial(0)
        self.assertEqual(result, 1)

    def test_factorial_one(self):
        """Test if factorial(1) returns 1"""
        result = factorial(1)
        self.assertEqual(result, 1)

    def test_factorial_positive(self):
        """Test if factorial function calculates the correct factorial"""
        test_cases = {
            2: 2,
            3: 6,
            4: 24,
            5: 120
        }
        for n, expected in test_cases.items():
            result = factorial(n)
            self.assertEqual(result, expected)

    def test_factorial_large(self):
        """Test if factorial function calculates large factorials correctly"""
        result = factorial(10)
        self.assertEqual(result, 3628800)

if __name__ == '__main__':
    unittest.main()
