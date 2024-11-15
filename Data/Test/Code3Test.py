import sys
import os
import inspect

def compare_functions():
    """
    Compares two files containing a BPlusTree and StudentDatabase class:
    - Checks if function names (including __init__) match.
    - Checks if function implementations match.
    Returns True if both match; False otherwise.
    """
    try:
        # test BPlusTree and StudentDatabase classes
        
        correct_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        buggy_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

        sys.path.append(correct_path)
        from Correct import Code3Correct as correct
        sys.path.remove(correct_path)

        sys.path.append(buggy_path)
        from Buggy import Code3Buggy as buggy
        sys.path.remove(buggy_path)
        
        correct_functions = inspect.getmembers(correct.BPlusTree, inspect.isfunction)
        buggy_functions = inspect.getmembers(buggy.BPlusTree, inspect.isfunction)

        # Check if the number of functions is the same
        if len(correct_functions) != len(buggy_functions):
            print("Different number of functions in BPlusTree class.")
            return False

        # Compare functions of BPlusTree
        for i in range(len(correct_functions)):
            if correct_functions[i][0] != buggy_functions[i][0]:
                print(f"Function names do not match: {correct_functions[i][0]} != {buggy_functions[i][0]}")
                return False

            # Check if implementations match
            correct_func_code = inspect.getsource(correct_functions[i][1])
            buggy_func_code = inspect.getsource(buggy_functions[i][1])

            if correct_func_code != buggy_func_code:
                print(f"Function implementations do not match for {correct_functions[i][0]}")
                return False
            
            if correct_functions[i][0] != '__init__':
                output_correct = correct_functions         
                output_buggy = buggy_functions 
                if output_correct != output_buggy:
                    print(f"Function output does not match for {correct_functions[i][0]}")
                    return False

        # Now, compare StudentDatabase class
        correct_functions = inspect.getmembers(correct.StudentDatabase, inspect.isfunction)
        buggy_functions = inspect.getmembers(buggy.StudentDatabase, inspect.isfunction)

        if len(correct_functions) != len(buggy_functions):
            print("Different number of functions in StudentDatabase class.")
            return False

        for i in range(len(correct_functions)):
            if correct_functions[i][0] != buggy_functions[i][0]:
                print(f"Function names do not match in StudentDatabase: {correct_functions[i][0]} != {buggy_functions[i][0]}")
                return False

            correct_func_code = inspect.getsource(correct_functions[i][1])
            buggy_func_code = inspect.getsource(buggy_functions[i][1])

            if correct_func_code != buggy_func_code:
                print(f"Function implementations do not match for {correct_functions[i][0]} in StudentDatabase")
                return False
            
            if correct_functions[i][0] != '__init__':
                output_correct = correct_functions 
                output_buggy = buggy_functions 
            
                if output_correct != output_buggy:
                    print(f"Function output does not match for {correct_functions[i][0]} in StudentDatabase")
                    return False

        return True
    
    except Exception as e:
        print(str(e))
        return False

# Run the comparison
if __name__ == "__main__":
    print(compare_functions())
