# filename: Code14Buggy.py
import random

class RockPaperScissors:
    def __init__(self):
        # Fixed the bug here by initializing available choices for the game
        self.choices = ['rock', 'paper', 'scissors']

    def play_round(self, player_choice):
        if player_choice not in self.choices:
            return "Invalid choice. Choose 'rock', 'paper', or 'scissors'."
        
        computer_choice = random.choice(self.choices)
        print(f"Computer chose: {computer_choice}")

        if player_choice == computer_choice:
            return "It's a tie!"
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "scissors" and computer_choice == "paper") or \
             (player_choice == "paper" and computer_choice == "rock"):
            return "You win!"
        else:
            return "You lose!"
