import tkinter as tk
from tkinter import *

player = 0  # 0 for player X, 1 for player O


class Mancala:
    def __init__(self, root):
        # This creates the main thing and calls necessary methods
        self.root = root
        self.root.title("Mancala")
        self.create_widgets()
        self.create_grid()

    def create_widgets(self):
        # This creates the starting text to welcome the player
        self.welcome_label = tk.Label(self.root, text="Welcome to Mancala", font=('Arial', 24))
        self.welcome_label.pack(pady=10)  # Add some vertical padding

    def create_grid(self):
        # Create a frame to hold the grid, and insert a wood grain color
        self.frame = tk.Frame(self.root, bg="#A1662F")
        self.frame.pack(pady=20)  # Add vertical padding around the frame

        # Define a 2x8 grid for the buttons (2 rows of game buttons, plus space for the goal buttons)
        self.buttons = [[None for _ in range(8)] for _ in range(2)]  # 2 rows, 8 columns

        # Goal 1 button (left side) - placed at column 0
        goal_left = tk.Button(self.frame, text="Goal 1", font=('Arial', 24), width=5, height=5,
                              command=lambda: self.on_button_click(None, 0))  # Goal button doesn't have stones
        goal_left.grid(row=0, column=0, rowspan=2, padx=5, pady=5)

        # Regular buttons for the first row (Pockets)
        for col in range(6):  # Loop over 6 columns (columns 1 to 6)
            button = tk.Button(self.frame, text='4', font=('Arial', 24), width=5, height=2)
            button.grid(row=0, column=col + 1, padx=5, pady=5)
            # Pass the button reference using the lambda function
            button.config(command=lambda r=0, c=col + 1, btn=button: self.on_button_click(r, c, btn))
            self.buttons[0][col + 1] = button  # Store button reference

        # Goal 2 button (right side) - placed at column 7
        goal_right = tk.Button(self.frame, text="Goal 2", font=('Arial', 24), width=5, height=5,
                               command=lambda: self.on_button_click(None, 7))  # Goal button doesn't have stones
        goal_right.grid(row=0, column=7, rowspan=2, padx=5, pady=5)

        # Regular buttons for the second row (Pockets)
        for col in range(6):  # Loop over 6 columns (columns 1 to 6)
            button = tk.Button(self.frame, text='4', font=('Arial', 24), width=5, height=2)
            button.grid(row=1, column=col + 1, padx=5, pady=5)
            # Pass the button reference using the lambda function
            button.config(command=lambda r=1, c=col + 1, btn=button: self.on_button_click(r, c, btn))
            self.buttons[1][col + 1] = button  # Store button reference

    def on_button_click(self, row, col, button=None):
        # Handle button clicks
        if button:  # If a game button was clicked
            print(f"Button clicked at row {row}, col {col}")
            print(f"That button has {button.cget('text')} stones in it")
        else:  # If a goal button was clicked
            print(f"Goal button clicked at row {row}, col {col}")


def main():
    root = tk.Tk()  # Create the main window
    Mancala(root)  # Initialize the game
    root.mainloop()  # Start the loop


if True:
    main()  # Run the application
