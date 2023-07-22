# -*- coding: utf-8 -*-
import random

class DiceRollingGame:
    def __init__(self):
        self.player_name = ""
        self.score = 0

    def get_player_name(self):
        # Get the player's name as input
        self.player_name = input("Enter your name: ")

    def roll_dice(self):
        # Roll the dice and return the result
        return random.randint(1, 6)

    def play(self):
        # Start the game
        print(f"Welcome, {self.player_name}! Let's play the Dice Rolling Game.")
        print("Instructions: Roll the dice and try to get the highest score!")

        while True:
            play_again = input("Press Enter to roll the dice or type 'exit' to quit: ")

            if play_again.lower() == 'exit':
                # Player decides to quit the game
                print("Thanks for playing! Your final score:", self.score)
                break

            roll_result = self.roll_dice()
            print(f"You rolled a {roll_result}!")

            if roll_result == 6:
                # Player rolled a 6 (highest score)
                print("Congratulations! You got the highest score!")
                self.score += 6
            else:
                # Player did not roll a 6
                print("Try again to get a higher score.")

def main():
    # Create an instance of the DiceRollingGame class and start the game
    game = DiceRollingGame()
    game.get_player_name()
    game.play()

if __name__ == "__main__":
    main()
