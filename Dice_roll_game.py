# -*- coding: utf-8 -*-
import random

class DiceRollingGame:
    def __init__(self):
        self.player_name = ""
        self.score = 0
        self.num_rolls = 0
        self.num_sides = 6  # Default number of sides on the dice

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

    def roll_dice(self):
        # Roll the dice and return the result
        return random.randint(1, self.num_sides)

    def play(self):
        # Start the game
        print(f"Welcome, {self.player_name}! Let's play the Dice Rolling Game.")
        print("Instructions: Roll the dice and try to get the highest score!")

        while True:
            play_again = input("Press Enter to roll the dice or type 'exit' to quit: ")

            if play_again.lower() == 'exit':
                # Player decides to quit the game
                print(f"Thanks for playing, {self.player_name}!")
                print(f"You rolled the dice {self.num_rolls} times.")
                print("Your final score:", self.score)
                break

            roll_result = self.roll_dice()
            print(f"You rolled a {roll_result}!")
            self.num_rolls += 1

            if roll_result == self.num_sides:
                # Player rolled the highest possible number
                print("Congratulations! You got the highest score!")
                self.score += self.num_sides
            else:
                # Player did not roll the highest possible number
                print("Try again to get a higher score.")

def main():
    # Create an instance of the DiceRollingGame class and start the game
    game = DiceRollingGame()
    game.get_player_name()
    game.get_num_sides()
    game.play()

if __name__ == "__main__":
    main()
