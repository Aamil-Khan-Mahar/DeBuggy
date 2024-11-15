import sys
import os
import inspect


def compare_functions():
    """
    Compares two files containing a Math class:
    - Checks if function names (including __init__) match.
    - Checks if function implementations match.
    Returns True if both match; False otherwise.
    """
    try:
        # test Math class
        
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

        # Testing all functions
        
        for i in range(len(correct_functions)):
            if correct_functions[i][0] != buggy_functions[i][0]:
                print("Function names do not match.")
                return False

            # Check if implementations match
            correct_func_code = inspect.getsource(correct_functions[i][1])
            buggy_func_code = inspect.getsource(buggy_functions[i][1])

            if correct_func_code != buggy_func_code:
                print("Function implementations do not match.")
                return False
            
            if correct_functions[i][0] != '__init__':
                ouput_correct = correct_functions[i][1](2, 3)
                ouput_buggy = buggy_functions[i][1](2, 3)
            
                if ouput_correct != ouput_buggy:
                    print("Function output does not match.")
                    return False
            
        return True
    
    except Exception as e:
        print(str(e))
        return False

# Run the comparison
if __name__ == "__main__":
    print(compare_functions())