import os
import sys
import inspect

def compare_functions():
    """
    Compares two files containing a DiceGame class:
    - Checks if function names (including __init__) match.
    - Checks if function outputs match when functions are called on instances.
    Returns True if both match; False otherwise.
    """
    try:
        correct_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Correct'))
        buggy_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Buggy'))

        sys.path.append(correct_path)
        from Correct import DiceGame as CorrectDiceGame
        sys.path.remove(correct_path)

        sys.path.append(buggy_path)
        from Buggy import DiceGame as BuggyDiceGame
        sys.path.remove(buggy_path)

        correct_functions = inspect.getmembers(CorrectDiceGame, inspect.isfunction)
        buggy_functions = inspect.getmembers(BuggyDiceGame, inspect.isfunction)

        if len(correct_functions) != len(buggy_functions):
            print("Different number of functions in DiceGame class.")
            return False
            
        players = ["Alice", "Bob", "Charlie"]
        correct_instance = CorrectDiceGame(players)
        buggy_instance = BuggyDiceGame(players)

        for i in range(len(correct_functions)):
            if correct_functions[i][0] != buggy_functions[i][0]:
                print(f"Function names do not match: {correct_functions[i][0]} != {buggy_functions[i][0]}")
                return False

            if correct_functions[i][0] != '__init__':
                if correct_functions[i][0] == "roll_dice":
                    output_correct = correct_functions[i][1](correct_instance)
                    output_buggy = buggy_functions[i][1](buggy_instance)

                    if not (1 <= output_correct <= 6) or not (1 <= output_buggy <= 6):
                        print(f"Function roll_dice returned an invalid output.")
                        return False

                elif correct_functions[i][0] == "play_round":
                    correct_functions[i][1](correct_instance)
                    buggy_functions[i][1](buggy_instance)

                    if correct_instance.scores != buggy_instance.scores:
                        print("Scores after play_round do not match.")
                        return False

                elif correct_functions[i][0] == "get_winner":
                    output_correct = correct_functions[i][1](correct_instance)
                    output_buggy = buggy_functions[i][1](buggy_instance)

                    if output_correct != output_buggy:
                        print("Winners and max score do not match.")
                        return False

        return True

    except Exception as e:
        print(str(e))
        return False

if __name__ == "__main__":
    print(compare_functions())

