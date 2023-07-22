# -*- coding: utf-8 -*-
import random
import tkinter as tk
from tkinter import messagebox

class DiceRollingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Dice Rolling Game")
        self.root.geometry("500x400")

        self.players = []
        self.num_players = 2
        self.target_rolls = 10
        self.num_sides = 6
        self.total_rounds = 0
        self.num_rolls = 0

        self.create_widgets()

    def create_widgets(self):
        # Create labels, entry, and buttons for the GUI
        self.title_label = tk.Label(self.root, text="Dice Rolling Game", font=("Helvetica", 20, "bold"))
        self.title_label.pack(pady=10)

        self.players_label = tk.Label(self.root, text="Enter number of players:")
        self.players_label.pack()
        self.players_entry = tk.Entry(self.root, width=5)
        self.players_entry.pack()

        self.rolls_label = tk.Label(self.root, text="Enter number of rolls per player:")
        self.rolls_label.pack()
        self.rolls_entry = tk.Entry(self.root, width=5)
        self.rolls_entry.pack()

        self.start_button = tk.Button(self.root, text="Start Game", command=self.start_game)
        self.start_button.pack(pady=10)

        self.roll_frame = tk.Frame(self.root)
        self.roll_frame.pack()

        self.result_label = tk.Label(self.root, text="", font=("Arial", 16))
        self.result_label.pack(pady=20)

    def start_game(self):
        # Start the game with specified number of players and target rolls
        try:
            self.num_players = int(self.players_entry.get())
            self.target_rolls = int(self.rolls_entry.get())
            if self.num_players <= 0 or self.target_rolls <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for players and rolls.")
            return

        # Create player list with initial scores and highest scores
        self.players = [{"name": f"Player {i+1}", "score": 0, "highest_score": 0} for i in range(self.num_players)]
        self.total_rounds = 0
        self.num_rolls = 0

        # Remove input elements and start button after starting the game
        self.players_label.pack_forget()
        self.players_entry.pack_forget()
        self.rolls_label.pack_forget()
        self.rolls_entry.pack_forget()
        self.start_button.pack_forget()

        # Create "Roll Dice" buttons for each player
        for player in self.players:
            self.create_roll_button(player["name"])

    def create_roll_button(self, player_name):
        # Create a "Roll Dice" button for the given player
        roll_button = tk.Button(self.roll_frame, text=f"Roll Dice for {player_name}", command=lambda: self.roll_dice(player_name))
        roll_button.pack(pady=5)

    def roll_dice(self, player_name):
        # Roll the dice for the given player and update scores
        roll_result = random.randint(1, self.num_sides)
        self.result_label.config(text=f"{player_name} rolled a {roll_result}!")

        for player in self.players:
            if player["name"] == player_name:
                if roll_result == self.num_sides:
                    player["score"] += self.num_sides
                    self.result_label.config(text=f"Congratulations, {player_name}! You win this round!")

                self.num_rolls += 1
                if self.num_rolls == self.target_rolls:
                    self.total_rounds += 1
                    self.num_rolls = 0
                    if self.total_rounds == self.num_players * self.target_rolls:
                        self.end_game()
                break

    def end_game(self):
        # Display the winner(s) of the game
        self.roll_frame.pack_forget()
        max_score = max(player["score"] for player in self.players)
        winners = [player["name"] for player in self.players if player["score"] == max_score]

        if len(winners) == 1:
            self.result_label.config(text=f"Congratulations, {winners[0]}! You are the winner!")
        else:
            self.result_label.config(text="It's a tie! The winners are:\n" + "\n".join(winners))

def main():
    root = tk.Tk()
    game = DiceRollingGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()