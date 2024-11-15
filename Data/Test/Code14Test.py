import unittest
from unittest.mock import patch
from Code14Correct.py import RockPaperScissors  

class TestRockPaperScissors(unittest.TestCase):

    # Test case for valid choices
    @patch('random.choice', return_value='rock')  # Mocking random.choice to always return 'rock'
    def test_play_round_tie(self, mock_random_choice):
        game = RockPaperScissors()
        result = game.play_round('rock')
        self.assertEqual(result, "It's a tie!")
        mock_random_choice.assert_called_with(["rock", "paper", "scissors"])

    @patch('random.choice', return_value='scissors')
    def test_play_round_win(self, mock_random_choice):
        game = RockPaperScissors()
        result = game.play_round('rock')
        self.assertEqual(result, "You win!")
        mock_random_choice.assert_called_with(["rock", "paper", "scissors"])

    @patch('random.choice', return_value='paper')
    def test_play_round_lose(self, mock_random_choice):
        game = RockPaperScissors()
        result = game.play_round('rock')
        self.assertEqual(result, "You lose!")
        mock_random_choice.assert_called_with(["rock", "paper", "scissors"])

    # Test invalid choice
    def test_invalid_choice(self):
        game = RockPaperScissors()
        result = game.play_round('lizard')  # Invalid choice
        self.assertEqual(result, "Invalid choice. Choose 'rock', 'paper', or 'scissors'.")

if __name__ == '__main__':
    unittest.main()

