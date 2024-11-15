import sys
import os
import inspect
import math

def compare_functions():
    """
    Compares the area calculation functions from both the correct and buggy code:
    - Checks if function names and logic match.
    - Tests if the functions return the expected results for various inputs.
    Returns True if both match; False otherwise.
    """
    try:
        # Test both the correct and buggy versions of the functions
        correct_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        buggy_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

        sys.path.append(correct_path)
        from Correct.Code11Correct import calculate_circle_area, calculate_rectangle_area, calculate_triangle_area
        sys.path.remove(correct_path)

        sys.path.append(buggy_path)
        from Buggy.Code11Buggy import calculate_circle_area as buggy_calculate_circle_area
        from Buggy.Code11Buggy import calculate_rectangle_area as buggy_calculate_rectangle_area
        from Buggy.Code11Buggy import calculate_triangle_area as buggy_calculate_triangle_area
        sys.path.remove(buggy_path)

        # Test cases for circle area
        correct_circle_area = calculate_circle_area(5)
        buggy_circle_area = buggy_calculate_circle_area(5)

        # Test cases for rectangle area
        correct_rectangle_area = calculate_rectangle_area(4, 6)
        buggy_rectangle_area = buggy_calculate_rectangle_area(4, 6)

        # Test cases for triangle area
        correct_triangle_area = calculate_triangle_area(3, 7)
        buggy_triangle_area = buggy_calculate_triangle_area(3, 7)

        # Compare results for each shape
        if correct_circle_area != buggy_circle_area:
            print(f"Circle area mismatch: Correct: {correct_circle_area}, Buggy: {buggy_circle_area}")
            return False
        if correct_rectangle_area != buggy_rectangle_area:
            print(f"Rectangle area mismatch: Correct: {correct_rectangle_area}, Buggy: {buggy_rectangle_area}")
            return False
        if correct_triangle_area != buggy_triangle_area:
            print(f"Triangle area mismatch: Correct: {correct_triangle_area}, Buggy: {buggy_triangle_area}")
            return False

        # Additional tests for negative values to check error handling
        correct_negative_circle = calculate_circle_area(-5)
        buggy_negative_circle = buggy_calculate_circle_area(-5)
        if correct_negative_circle != buggy_negative_circle:
            print(f"Negative circle area mismatch: Correct: {correct_negative_circle}, Buggy: {buggy_negative_circle}")
            return False

        correct_negative_rectangle = calculate_rectangle_area(-4, 6)
        buggy_negative_rectangle = buggy_calculate_rectangle_area(-4, 6)
        if correct_negative_rectangle != buggy_negative_rectangle:
            print(f"Negative rectangle area mismatch: Correct: {correct_negative_rectangle}, Buggy: {buggy_negative_rectangle}")
            return False

        correct_negative_triangle = calculate_triangle_area(3, -7)
        buggy_negative_triangle = buggy_calculate_triangle_area(3, -7)
        if correct_negative_triangle != buggy_negative_triangle:
            print(f"Negative triangle area mismatch: Correct: {correct_negative_triangle}, Buggy: {buggy_negative_triangle}")
            return False

        return True
    
    except Exception as e:
        print(f"Error during comparison: {str(e)}")
        return False


# Run the comparison
if __name__ == "__main__":
    print(compare_functions())
