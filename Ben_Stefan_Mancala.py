import tkinter as tk
from tkinter import messagebox

player = 0  # 0 for player X, 1 for player O

class Mancala:
    def __init__(self, root):
        # this creates the main thing and calls necessary methods
        self.root = root
        self.root.title("Mancala")
        self.create_widgets()
        self.create_grid()

    def create_widgets(self):
        # this creates the starting text to welcome the player
        self.welcome_label = tk.Label(self.root, text="Welcome to Mancala", font=('Arial', 24))
        self.welcome_label.pack(pady=10)  # Add some vertical padding

    def create_grid(self):
        # Create a frame to hold the grid
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)  # Add vertical padding around the frame

        # Define a 3x8 grid for the buttons (2 rows of game buttons, plus space for the goal buttons)
        self.buttons = [[None for _ in range(8)] for _ in range(3)]  # 3 rows, 8 columns

        # Goal 1 button (left side) - placed at column 0
        goal_left = tk.Button(self.frame, text="Goal 1", font=('Arial', 24), width=5, height=7,
                              command=lambda: self.on_button_click(1, 0))  # Fixed lambda function
        goal_left.grid(row=1, column=0, rowspan=1, padx=5, pady=5)  # Stretch vertically across both rows

        # Regular buttons for the first row (Game buttons)
        for col in range(6):  # Loop over 6 columns (columns 1 to 6)
            button = tk.Button(self.frame, text='4', font=('Arial', 24), width=5, height=2,
                               command=lambda r=0, c=col+1: self.on_button_click(r, c))  # Pass row and col correctly
            button.grid(row=0, column=col+1, padx=5, pady=5)  # Place at columns 1 to 6 (col+1)
            self.buttons[1][col+1] = button  # Store the button reference

        # Goal 2 button (right side) - placed at column 7
        goal_right = tk.Button(self.frame, text="Goal 2", font=('Arial', 24), width=5, height=7,
                               command=lambda: self.on_button_click(1, 7))  # Fixed lambda function
        goal_right.grid(row=1, column=7, rowspan=1, padx=5, pady=5)  # Stretch vertically across both rows

        # Regular buttons for the second row (Game buttons)
        for col in range(6):  # Loop over 6 columns (columns 1 to 6)
            button = tk.Button(self.frame, text='4', font=('Arial', 24), width=5, height=2,
                               command=lambda r=2, c=col+1: self.on_button_click(r, c))  # Pass row and col correctly
            button.grid(row=2, column=col+1, padx=5, pady=5)  # Place at columns 1 to 6 (col+1)
            self.buttons[2][col+1] = button  # Store the button reference

    def on_button_click(self, row, col):
        # This is a placeholder function for when a button is clicked
        print(f"Button clicked at row {row}, col {col}")

def main():
    root = tk.Tk()  # Create the main window
    Mancala(root)  # Initialize the game
    root.mainloop()  # Start the loop


if True:
    main()  # Run the application
