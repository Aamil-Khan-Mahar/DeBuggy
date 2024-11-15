import sys
import os
import inspect

def compare_functions():
    """
    Compares two versions of bubble_sort and binary_search:
    - Checks if function names (including bubble_sort and binary_search) match.
    - Checks if function implementations match.
    Returns True if both match; False otherwise.
    """
    try:
        # test bubble_sort and binary_search
        
        correct_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        buggy_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

        sys.path.append(correct_path)
        from Correct.Code8Correct import bubble_sort, binary_search
        sys.path.remove(correct_path)

        sys.path.append(buggy_path)
        from Buggy.Code8Buggy import bubble_sort as buggy_bubble_sort, binary_search as buggy_binary_search
        sys.path.remove(buggy_path)

        correct_functions = [bubble_sort, binary_search]
        buggy_functions = [buggy_bubble_sort, buggy_binary_search]

        # Check if the number of functions is the same
        if len(correct_functions) != len(buggy_functions):
            print("Different number of functions in bubble_sort and binary_search.")
            return False

        # Compare functions bubble_sort and binary_search
        for i in range(len(correct_functions)):
            if correct_functions[i].__name__ != buggy_functions[i].__name__:
                print(f"Function names do not match: {correct_functions[i].__name__} != {buggy_functions[i].__name__}")
                return False

            # Check if implementations match
            correct_func_code = inspect.getsource(correct_functions[i])
            buggy_func_code = inspect.getsource(buggy_functions[i])

            if correct_func_code != buggy_func_code:
                print(f"Function implementations do not match for {correct_functions[i].__name__}")
                return False

        # Test correctness by running both implementations
        correct_bubble_sort_output = bubble_sort([64, 34, 25, 12, 22, 11, 90])
        buggy_bubble_sort_output = buggy_bubble_sort([64, 34, 25, 12, 22, 11, 90])
        
        if correct_bubble_sort_output != buggy_bubble_sort_output:
            print(f"bubble_sort outputs do not match.")
            return False

        correct_binary_search_output = binary_search(correct_bubble_sort_output, 22)
        buggy_binary_search_output = buggy_binary_search(buggy_bubble_sort_output, 22)

        if correct_binary_search_output != buggy_binary_search_output:
            print(f"binary_search outputs do not match.")
            return False

        return True
    
    except Exception as e:
        print(str(e))
        return False

# Run the comparison
if __name__ == "__main__":
    print(compare_functions())
