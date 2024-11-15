import sys
import os
import inspect

# Define the correct and buggy paths

def compare_functions():
    """
    Compares the functions between two classes named FlightTracker in Code1Correct and Code1Buggy.
    - Checks if function names match.
    - Checks if function implementations match.
    - Checks if the output of the functions is the same.
    """
    try:
        correct_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        buggy_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

        # Add Correct path and try importing the Code1Correct module
        sys.path.append(correct_path)
        from Correct import Code2Correct as correct
        sys.path.remove(correct_path)

        # Add Buggy path and try importing the Code1Buggy module
        sys.path.append(buggy_path)
        from Buggy import Code2Buggy as buggy
        sys.path.remove(buggy_path)
        # Get all functions (including __init__) in both Math classes using inspect
        correct_functions = inspect.getmembers(correct.FlightTracker, inspect.isfunction)
        buggy_functions = inspect.getmembers(buggy.FlightTracker, inspect.isfunction)

        # Check if both classes have the same number of functions
        if len(correct_functions) != len(buggy_functions):
            print("Different number of functions in FlightTracker class.")
            return False

        # Test if function names and implementations match
        for correct_func, buggy_func in zip(correct_functions, buggy_functions):
            # Function name comparison
            if correct_func[0] != buggy_func[0]:
                print(f"Function names do not match: {correct_func[0]} vs {buggy_func[0]}")
                return False

            # Compare function implementations
            correct_func_code = inspect.getsource(correct_func[1]).strip()
            buggy_func_code = inspect.getsource(buggy_func[1]).strip()

            if correct_func_code != buggy_func_code:
                print(f"Function implementation does not match for: {correct_func[0]}")
                return False
            
            # If not '__init__', compare output
            if correct_func[0] != '__init__':
                # Assuming that the methods take `flights` data
                test_data = {
                    'numbers': [1001, 1002],
                    'origins': ['NYC', 'LA'],
                    'destinations': ['LA', 'NYC'],
                    'durations': [5, 4],
                    'prices': [200, 250],
                    'dates': ['2024-11-10', '2024-11-11'],
                    'times': ['12:00', '14:00'],
                    'airlines': ['Delta', 'American'],
                    'planes': ['Boeing 737', 'Airbus A320'],
                    'seats': [100, 120],
                    'classes': ['Economy', 'Business'],
                    'passengers': [90, 110],
                    'status': ['On Time', 'Delayed'],
                    'captain': ['John Doe', 'Jane Smith']
                }

                # Creating instances of the classes with test data
                correct_instance = correct.FlightTracker(test_data)
                buggy_instance = buggy.FlightTracker(test_data)

                try:
                    correct_output = getattr(correct_instance, correct_func[0])()
                    buggy_output = getattr(buggy_instance, buggy_func[0])()
                except Exception as e:
                    print(f"Error when calling {correct_func[0]}: {e}")
                    return False

                if correct_output != buggy_output:
                    print(f"Output mismatch for function: {correct_func[0]}")
                    return False

        return True
    
    except Exception as e:
        return False

# Run the comparison
if __name__ == "__main__":
    print(compare_functions())