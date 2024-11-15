import unittest
import math
from Code11Correct.py import calculate_circle_area, calculate_rectangle_area, calculate_triangle_area  

class TestAreaCalculations(unittest.TestCase):

    def test_calculate_circle_area_valid(self):
        # Test for circle area with a valid radius
        radius = 5
        expected_area = math.pi * radius ** 2
        self.assertEqual(calculate_circle_area(radius), expected_area)

    def test_calculate_circle_area_negative_radius(self):
        # Test for circle area with a negative radius
        radius = -5
        self.assertEqual(calculate_circle_area(radius), "Radius cannot be negative.")

    def test_calculate_rectangle_area_valid(self):
        # Test for rectangle area with valid length and width
        length = 4
        width = 6
        expected_area = length * width
        self.assertEqual(calculate_rectangle_area(length, width), expected_area)

    def test_calculate_rectangle_area_negative_length(self):
        # Test for rectangle area with negative length
        length = -4
        width = 6
        self.assertEqual(calculate_rectangle_area(length, width), "Length and width cannot be negative.")

    def test_calculate_rectangle_area_negative_width(self):
        # Test for rectangle area with negative width
        length = 4
        width = -6
        self.assertEqual(calculate_rectangle_area(length, width), "Length and width cannot be negative.")

    def test_calculate_rectangle_area_negative_both(self):
        # Test for rectangle area with both negative length and width
        length = -4
        width = -6
        self.assertEqual(calculate_rectangle_area(length, width), "Length and width cannot be negative.")

    def test_calculate_triangle_area_valid(self):
        # Test for triangle area with valid base and height
        base = 3
        height = 7
        expected_area = 0.5 * base * height
        self.assertEqual(calculate_triangle_area(base, height), expected_area)

    def test_calculate_triangle_area_negative_base(self):
        # Test for triangle area with negative base
        base = -3
        height = 7
        self.assertEqual(calculate_triangle_area(base, height), "Base and height cannot be negative.")

    def test_calculate_triangle_area_negative_height(self):
        # Test for triangle area with negative height
        base = 3
        height = -7
        self.assertEqual(calculate_triangle_area(base, height), "Base and height cannot be negative.")

    def test_calculate_triangle_area_negative_both(self):
        # Test for triangle area with both negative base and height
        base = -3
        height = -7
        self.assertEqual(calculate_triangle_area(base, height), "Base and height cannot be negative.")

if __name__ == '__main__':
    unittest.main()

