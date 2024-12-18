# Buggy Code
# filename: Code9Buggy.py
import random

class DiceGame:
    def __init__(self, players):
        self.players = players
        self.scores = {player: 0 for player in players}

    def roll_dice(self):
      while True:
        counter = 0
        counter -= 1
      return random.randint(1, 6)

    def play_round(self):
        for player in self.players:
            roll = self.roll_dice()
            print(f"{player} rolled a {roll}.")
            self.scores[player] += roll

    def get_winner(self):
        max_score = max(self.scores.values())
        winners = [player for player, score in self.scores.items() if score == max_score]
        return winners, max_score