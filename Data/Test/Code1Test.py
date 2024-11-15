import sys
import os
import inspect


import os
import sys
import inspect

def compare_functions():
    """
    Compares two files containing a Math class:
    - Checks if function names (including __init__) match.
    - Checks if function outputs match when functions are called on instances.
    Returns True if both match; False otherwise.
    """
    try:
        correct_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        buggy_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

        sys.path.append(correct_path)
        from Correct import Code1Correct as correct
        sys.path.remove(correct_path)

        sys.path.append(buggy_path)
        from Buggy import Code1Buggy as buggy
        sys.path.remove(buggy_path)
        
        correct_functions = inspect.getmembers(correct.Math, inspect.isfunction)
        buggy_functions = inspect.getmembers(buggy.Math, inspect.isfunction)

        if len(correct_functions) != len(buggy_functions):
            print("Different number of functions in Math class.")
            return False

        for i in range(len(correct_functions)):
            if correct_functions[i][0] != buggy_functions[i][0]:
                print("Function names do not match.")
                return False

            correct_instance = correct.Math()
            buggy_instance = buggy.Math()

            if correct_functions[i][0] != '__init__':  
                output_correct = correct_functions[i][1](correct_instance, 2, 3)
                output_buggy = buggy_functions[i][1](buggy_instance, 2, 3)

                if output_correct != output_buggy:
                    print(f"Function {correct_functions[i][0]} output does not match.")
                    return False

        return True
    
    except Exception as e:
        print(str(e))
        return False

if __name__ == "__main__":
    print(compare_functions())
