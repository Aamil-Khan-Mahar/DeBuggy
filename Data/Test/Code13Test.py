import sys
import os

def compare_functions():
    """
    Compares the fibonacci and factorial function from both the correct and buggy code:
    - Checks if function outputs match for the same inputs.
    Returns True if both match; False otherwise.
    """
    try:
        # Test both the correct and buggy versions of the fibonacci and factorial functions
        correct_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        buggy_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

        sys.path.append(correct_path)
        from Correct import fibonacci as CorrectFibonacci, factorial as CorrectFactorial
        sys.path.remove(correct_path)

        sys.path.append(buggy_path)
        from Buggy import fibonacci as BuggyFibonacci, factorial as BuggyFactorial
        sys.path.remove(buggy_path)

        # Test cases for correct functionality
        # Fibonacci test
        fibonacci_test_cases = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        factorial_test_cases = [1, 2, 3, 4, 5]

        # Compare fibonacci outputs
        for n in fibonacci_test_cases:
            correct_fib = CorrectFibonacci(n)
            buggy_fib = BuggyFibonacci(n)
            if correct_fib != buggy_fib:
                print(f"Fibonacci mismatch for n={n}: Correct: {correct_fib}, Buggy: {buggy_fib}")
                return False

        # Compare factorial outputs
        for n in factorial_test_cases:
            correct_fact = CorrectFactorial(n)
            buggy_fact = BuggyFactorial(n)
            if correct_fact != buggy_fact:
                print(f"Factorial mismatch for n={n}: Correct: {correct_fact}, Buggy: {buggy_fact}")
                return False

        return True
    
    except Exception as e:
        print(f"Error during comparison: {str(e)}")
        return False


# Run the comparison
if __name__ == "__main__":
    print(compare_functions())
