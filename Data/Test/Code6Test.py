import os
import sys
import inspect

def compare_functions():
    """
    Compares two files containing a RelativeGrader class:
    - Checks if function names (including __init__) match.
    - Checks if function outputs match when functions are called on instances.
    Returns True if both match; False otherwise.
    """
    try:
        correct_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Correct'))
        buggy_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Buggy'))

        sys.path.append(correct_path)
        from Correct.Code6Correct import RelativeGrader as CorrectGrader
        sys.path.remove(correct_path)

        sys.path.append(buggy_path)
        from Buggy.Code6Buggy import RelativeGrader as BuggyGrader
        sys.path.remove(buggy_path)

        correct_functions = inspect.getmembers(CorrectGrader, inspect.isfunction)
        buggy_functions = inspect.getmembers(BuggyGrader, inspect.isfunction)

        if len(correct_functions) != len(buggy_functions):
            print("Different number of functions in RelativeGrader class.")
            return False

        correct_instance = CorrectGrader([
            {"name": "Alice", "grade": 85},
            {"name": "Bob", "grade": 90},
            {"name": "Charlie", "grade": 78},
        ])

        buggy_instance = BuggyGrader([
            {"name": "Alice", "grade": 85},
            {"name": "Bob", "grade": 90},
            {"name": "Charlie", "grade": 78},
        ])

        for i in range(len(correct_functions)):
            if correct_functions[i][0] != buggy_functions[i][0]:
                print(f"Function names do not match: {correct_functions[i][0]} != {buggy_functions[i][0]}")
                return False

            if correct_functions[i][0] != '__init__':
                # Prepare arguments based on the function's name for testing
                if correct_functions[i][0] in ["add_student", "remove_student"]:
                    student = {"name": "Daisy", "grade": 88}
                    correct_functions[i][1](correct_instance, student)
                    buggy_functions[i][1](buggy_instance, student)

                elif correct_functions[i][0] == "get_student":
                    output_correct = correct_functions[i][1](correct_instance, "Alice")
                    output_buggy = buggy_functions[i][1](buggy_instance, "Alice")

                elif correct_functions[i][0] == "update_grade":
                    correct_functions[i][1](correct_instance, "Alice", 95)
                    buggy_functions[i][1](buggy_instance, "Alice", 95)

                else:
                    output_correct = correct_functions[i][1](correct_instance)
                    output_buggy = buggy_functions[i][1](buggy_instance)

                if 'output_correct' in locals() and output_correct != output_buggy:
                    print(f"Function {correct_functions[i][0]} output does not match.")
                    return False

        return True

    except Exception as e:
        print(str(e))
        return False

if __name__ == "__main__":
    print(compare_functions())
