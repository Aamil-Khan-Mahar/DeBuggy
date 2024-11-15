import sys
import os

def compare_rock_paper_scissors():
    """
    Compares the play_round method of both the correct and buggy code:
    - Checks if the play_round method correctly handles valid inputs and returns appropriate results.
    Returns True if both match for all cases; False otherwise.
    """
    try:
        # Test cases for Rock, Paper, Scissors
        test_choices = ["rock", "paper", "scissors"]
        correct_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        buggy_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

        sys.path.append(correct_path)
        from Correct.Code14Correct import RockPaperScissors as CorrectRPS
        sys.path.remove(correct_path)

        sys.path.append(buggy_path)
        from Buggy.Code14Buggy import RockPaperScissors as BuggyRPS
        sys.path.remove(buggy_path)

        # Initialize game objects for correct and buggy code
        correct_game = CorrectRPS()
        buggy_game = BuggyRPS()

        # Test play_round for each choice
        for player_choice in test_choices:
            print(f"Testing with player choice: {player_choice}")
            
            # Compare correct and buggy results
            correct_result = correct_game.play_round(player_choice)
            buggy_result = buggy_game.play_round(player_choice)
            
            if correct_result != buggy_result:
                print(f"Mismatch for player choice '{player_choice}':")
                print(f"Correct: {correct_result}")
                print(f"Buggy: {buggy_result}")
                return False

        return True
    
    except Exception as e:
        print(f"Error during comparison: {str(e)}")
        return False


# Run the comparison
if __name__ == "__main__":
    print(compare_rock_paper_scissors())
