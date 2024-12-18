# filename: Code11Buggy.py
import math


def calculate_circle_area(radius):
    # Fixed logic by changing the condition from > to <=
    if radius <= 0:
        return "Radius cannot be zero or negative."
    return math.pi * radius ** 2


def calculate_rectangle_area(length, width):
    # Corrected the logic by changing conditions from < to <= for length and width
    if length <= 0 or width <= 0:
        return "Length and width cannot be zero or negative."
    return length * width


def calculate_triangle_area(base, height):
    # Corrected the logic by changing conditions from < to <= for base and height
    if base <= 0 or height <= 0:
        return "Base and height cannot be zero or negative."
    return 0.5 * base * height
