# Buggy Code

import math

def calculate_circle_area(radius):
    if radius > 0:
        return "Radius cannot be positive."
    return math.pi * radius ** 2

def calculate_rectangle_area(length, width):
    if length < 0 or width < 0:
        return "Length and width cannot be negative."
    return length * width

def calculate_triangle_area(base, height):
    if base < 0 or height < 0:
        return "Base and height cannot be negative."
    return 0.5 * base * height
