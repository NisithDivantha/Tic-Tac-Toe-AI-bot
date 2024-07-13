# Tic-Tac-Toe-AI-bot

Develop an AI bot that can play Tic-Tac-Toe at an optimal level using the Minimax algorithm. This project aims to practice the concepts of game AI, decision-making algorithms, and implementing AI in a simple game environment.

## Features

- Play Tic-Tac-Toe against an AI opponent
- AI opponent uses the Minimax algorithm to make optimal moves
- Graphical User Interface (GUI) built with Tkinter
- Modular code structure separating game logic and GUI

## Setup

### Prerequisites

- Python 3.x
- Tkinter (usually included with Python installations)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/NisithDivantha/Tic-Tac-Toe-AI-bot.git
   cd Tic-Tac-Toe-AI-bot
   
## Usage

### Running the Game
Ensure both tic_tac_toe.py and tic_tac_toe_gui.py are in the same directory.

- Run the GUI script: python tic_tac_toe_gui.py

### Running the Game Logic Separately
- Run the game logic script to test the AI without the GUI: python tic_tac_toe.py

## Game Logic Overview
The game logic is contained in tic_tac_toe.py and includes the following functions:

- initialize_board(): Initializes and returns an empty Tic-Tac-Toe board.
- print_board(board): Prints the current state of the board to the console.
- check_winner(board): Checks for a winner or a draw and returns the result.
- minimax(board, depth, is_maximizing): Implements the Minimax algorithm to determine the optimal move.
- best_move(board): Determines the best move for the AI to make based on the Minimax algorithm.

## GUI Overview
The GUI is built using Tkinter and is contained in tic_tac_toe_gui.py. 
It includes:

- TicTacToeApp: The main class for the GUI application.
- create_widgets(): Creates the buttons for the Tic-Tac-Toe board.
- player_move(r, c): Handles the player's move.
- ai_move(): Handles the AI's move.
- check_game_over(): Checks if the game is over and displays the result.
- reset_board(): Resets the board for a new game.
