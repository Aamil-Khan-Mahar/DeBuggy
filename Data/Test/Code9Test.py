
import unittest
from unittest.mock import patch
from Code9Correct.py import DiceGame  # Replace with the correct file name if needed

class TestDiceGame(unittest.TestCase):

    @patch('random.randint')
    def test_roll_dice(self, mock_randint):
        # Mocking the random roll to always return 3
        mock_randint.return_value = 3
        
        game = DiceGame(["Alice", "Bob", "Charlie"])
        
        # Test dice roll for each player
        self.assertEqual(game.roll_dice(), 3)
        
    @patch('random.randint')
    def test_play_round(self, mock_randint):
        # Mocking the dice rolls for each player to return fixed values
        mock_randint.side_effect = [3, 4, 2]  # Alice rolls 3, Bob rolls 4, Charlie rolls 2
        
        game = DiceGame(["Alice", "Bob", "Charlie"])
        
        # Playing a round and checking the scores
        game.play_round()
        
        # Check if the scores are updated correctly
        self.assertEqual(game.scores["Alice"], 3)
        self.assertEqual(game.scores["Bob"], 4)
        self.assertEqual(game.scores["Charlie"], 2)

    @patch('random.randint')
    def test_get_winner_single(self, mock_randint):
        # Mocking the dice rolls to ensure a clear winner
        mock_randint.side_effect = [5, 3, 2, 6, 4, 1, 6, 6, 4, 1]  # Rolls for 5 rounds
        
        game = DiceGame(["Alice", "Bob", "Charlie"])
        
        # Playing 5 rounds
        for _ in range(5):
            game.play_round()

        winners, score = game.get_winner()
        
        # Bob has the highest score (14)
        self.assertEqual(winners, ["Bob"])
        self.assertEqual(score, 14)

    @patch('random.randint')
    def test_get_winner_tie(self, mock_randint):
        # Mocking the dice rolls to ensure a tie between Alice and Charlie
        mock_randint.side_effect = [4, 3, 4, 4, 3, 3, 4, 3, 4, 4]  # Rolls for 5 rounds
        
        game = DiceGame(["Alice", "Bob", "Charlie"])
        
        # Playing 5 rounds
        for _ in range(5):
            game.play_round()

        winners, score = game.get_winner()
        
        # Alice and Charlie are tied with score 16
        self.assertEqual(winners, ["Alice", "Charlie"])
        self.assertEqual(score, 16)

    def test_initial_scores(self):
        game = DiceGame(["Alice", "Bob", "Charlie"])
        
        # Initial scores should all be 0
        self.assertEqual(game.scores["Alice"], 0)
        self.assertEqual(game.scores["Bob"], 0)
        self.assertEqual(game.scores["Charlie"], 0)

if __name__ == '__main__':
    unittest.main()
