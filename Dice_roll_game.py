# -*- coding: utf-8 -*-
import random

class DiceRollingGame:
    def __init__(self):
        # Initialize the list to store player information
        self.players = []
        self.num_players = 2  # Number of players (default: 2)
        self.num_rolls = 0
        self.total_rounds = 0
        self.target_rolls = 10  # Default number of rolls before the game ends
        self.num_sides = 6  # Default number of sides on the dice

        # Get the names of the players
        for i in range(self.num_players):
            player_name = input(f"Enter name of Player {i + 1}: ")
            player_info = {
                "name": player_name,
                "score": 0,
                "highest_score": 0
            }
            self.players.append(player_info)

    def roll_dice(self):
        # Roll the dice and return the result
        return random.randint(1, self.num_sides)

    def get_target_rolls(self):
        # Get the number of target rolls from the user
        while True:
            try:
                self.target_rolls = int(input("Enter the number of rolls per player: "))
                if self.target_rolls <= 0:
                    print("Please enter a positive number.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def play(self):
        # Start the game
        print("Welcome to the Dice Rolling Game!")
        self.get_target_rolls()
        self.num_rolls = 0

        # Loop until the target number of rolls is reached
        while self.total_rounds < self.target_rolls:
            # Iterate through each player in the players list
            for player in self.players:
                player_name = player["name"]
                player_score = player["score"]
                player_highest_score = player["highest_score"]

                play_again = input(f"{player_name}, press Enter to roll the dice or type 'exit' to quit: ")

                if play_again.lower() == 'exit':
                    # Player decides to quit the game
                    print(f"Thanks for playing, {player_name}!")
                    print(f"You played a total of {self.total_rounds} rounds.")
                    print(f"Your final score: {player_score}")
                    print(f"Your highest score: {player_highest_score}")
                    break

                # Roll the dice and display the result
                roll_result = self.roll_dice()
                print(f"{player_name}, you rolled a {roll_result}!")
                self.num_rolls += 1

                # Check if the player rolled the highest possible number (e.g., 6)
                if roll_result == self.num_sides:
                    print("Congratulations! You got the highest score this round!")
                    player_score += self.num_sides

                    # Update the player's highest score if necessary
                    if player_score > player_highest_score:
                        player["highest_score"] = player_score
                else:
                    print("Try again to get a higher score this round.")

            # All players have completed their rolls for this round
            else:
                self.total_rounds += 1
                print(f"Round {self.total_rounds} over!")
                self.num_rolls = 0

        # Game ends
        print("Game over!")

        # Determine and announce the winner at the end of the game
        max_score = max(player["score"] for player in self.players)
        winners = [player["name"] for player in self.players if player["score"] == max_score]

        if len(winners) == 1:
            print(f"\nCongratulations, {winners[0]}! You are the winner!")
        else:
            print("\nIt's a tie! The winners are:")
            for winner in winners:
                print(winner)

def main():
    # Create an instance of the DiceRollingGame class and start the game
    game = DiceRollingGame()
    game.play()

if __name__ == "__main__":
    main()