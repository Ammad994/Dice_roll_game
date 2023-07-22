# -*- coding: utf-8 -*-
import random

class DiceRollingGame:
    def __init__(self):
        self.player_name = ""
        self.score = 0
        self.highest_score = 0
        self.num_rolls = 0
        self.num_sides = 6  # Default number of sides on the dice
        self.target_rolls = 10  # Default number of rolls before the game ends

    def get_player_name(self):
        # Get the player's name as input
        self.player_name = input("Enter your name: ")

    def get_num_sides(self):
        # Get the number of sides on the dice as input
        while True:
            try:
                self.num_sides = int(input("Enter the number of sides on the dice (minimum 2): "))
                if self.num_sides < 2:
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Please enter a valid number of sides.")

    def get_target_rolls(self):
        # Get the number of rolls before the game ends as input
        while True:
            try:
                self.target_rolls = int(input("Enter the number of rolls before the game ends (minimum 1): "))
                if self.target_rolls < 1:
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Please enter a valid number of rolls.")

    def roll_dice(self):
        # Roll the dice and return the result
        return random.randint(1, self.num_sides)

    def play(self):
        # Start the game
        print(f"Welcome, {self.player_name}! Let's play the Dice Rolling Game.")
        print(f"You have {self.target_rolls} rolls to achieve the highest score!")

        while self.num_rolls < self.target_rolls:
            play_again = input("Press Enter to roll the dice or type 'exit' to quit: ")

            if play_again.lower() == 'exit':
                # Player decides to quit the game
                print(f"Thanks for playing, {self.player_name}!")
                print(f"You rolled the dice {self.num_rolls} times.")
                print("Your final score:", self.score)
                print("Your highest score:", self.highest_score)
                break

            roll_result = self.roll_dice()
            print(f"You rolled a {roll_result}!")
            self.num_rolls += 1

            if roll_result == self.num_sides:
                # Player rolled the highest possible number
                print("Congratulations! You got the highest score!")
                self.score += self.num_sides

                if self.score > self.highest_score:
                    self.highest_score = self.score
            else:
                # Player did not roll the highest possible number
                print("Try again to get a higher score.")

        else:
            # Player has reached the maximum number of rolls
            print("Game over! You have reached the maximum number of rolls.")

def main():
    # Create an instance of the DiceRollingGame class and start the game
    game = DiceRollingGame()
    game.get_player_name()
    game.get_num_sides()
    game.get_target_rolls()
    game.play()

if __name__ == "__main__":
    main()
