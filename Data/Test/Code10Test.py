import os
import sys
import inspect

def compare_functions():
    """
    Compares two files containing a BankAccount class:
    - Checks if function names (including __init__) match.
    - Checks if function outputs match when functions are called on instances.
    Returns True if both match; False otherwise.
    """
    try:
        correct_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Correct'))
        buggy_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Buggy'))

        sys.path.append(correct_path)
        from Correct.Code10Correct import BankAccount as CorrectBankAccount
        sys.path.remove(correct_path)

        sys.path.append(buggy_path)
        from Buggy.Code10Buggy import BankAccount as BuggyBankAccount
        sys.path.remove(buggy_path)

        correct_functions = inspect.getmembers(CorrectBankAccount, inspect.isfunction)
        buggy_functions = inspect.getmembers(BuggyBankAccount, inspect.isfunction)

        if len(correct_functions) != len(buggy_functions):
            print("Different number of functions in BankAccount class.")
            return False

        correct_instance = CorrectBankAccount("Alice", 100)
        buggy_instance = BuggyBankAccount("Alice", 100)

        for i in range(len(correct_functions)):
            if correct_functions[i][0] != buggy_functions[i][0]:
                print(f"Function names do not match: {correct_functions[i][0]} != {buggy_functions[i][0]}")
                return False

            if correct_functions[i][0] != '__init__':
                if correct_functions[i][0] == "deposit":
                    output_correct = correct_functions[i][1](correct_instance, 50)
                    output_buggy = buggy_functions[i][1](buggy_instance, 50)
                    if output_correct != output_buggy:
                        print(f"Function deposit output does not match: {output_correct} != {output_buggy}")
                        return False

                elif correct_functions[i][0] == "withdraw":
                    output_correct = correct_functions[i][1](correct_instance, 30)
                    output_buggy = buggy_functions[i][1](buggy_instance, 30)
                    if output_correct != output_buggy:
                        print(f"Function withdraw output does not match: {output_correct} != {output_buggy}")
                        return False

                elif correct_functions[i][0] == "check_balance":
                    output_correct = correct_functions[i][1](correct_instance)
                    output_buggy = buggy_functions[i][1](buggy_instance)
                    if output_correct != output_buggy:
                        print(f"Function check_balance output does not match: {output_correct} != {output_buggy}")
                        return False

        return True

    except Exception as e:
        print(str(e))
        return False

if __name__ == "__main__":
    print(compare_functions())

