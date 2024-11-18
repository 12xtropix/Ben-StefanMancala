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
        frame = tk.Frame(self.root)
        frame.pack(pady=20)  # Add some vertical padding

    def create_board(self):
        #creates the pockets and the mancalas

