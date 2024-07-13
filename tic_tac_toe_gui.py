import tkinter as tk
from tkinter import messagebox
from tic_tac_toe import initialize_board, check_winner, best_move

class TicTacToeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.board = initialize_board()
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_widgets()

    def create_widgets(self):
        for r in range(3):
            for c in range(3):
                button = tk.Button(self.root, text=' ', cursor='X_cursor', font=('Arial', 30), width=15, height=8,
                                   command=lambda r=r, c=c: self.player_move(r, c))
                button.grid(row=r, column=c)
                self.buttons[r][c] = button

    def player_move(self, r, c):
        if self.board[r][c] == ' ':
            self.board[r][c] = 'X'
            self.buttons[r][c].config(text='X', state='disabled')
            if self.check_game_over():
                return
            self.ai_move()

    def ai_move(self):
        move = best_move(self.board)
        if move:
            r, c = move
            self.board[r][c] = 'O'
            self.buttons[r][c].config(text='O', state='disabled')
            self.check_game_over()

    def check_game_over(self):
        winner = check_winner(self.board)
        if winner == 'X' :
            messagebox.showinfo("Game Over", "Human wins!")
            self.reset_board()
            return True
        elif winner == 'O':
            messagebox.showinfo("Game Over", "Computer wins!")
            self.reset_board()
            return True
        elif not any(' ' in row for row in self.board):
            messagebox.showinfo("Game Over", "It's a draw!")
            self.reset_board()
            return True
        return False

    def reset_board(self):
        self.board = initialize_board()
        for r in range(3):
            for c in range(3):
                self.buttons[r][c].config(text=' ', state='normal')

if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeApp(root)
    root.mainloop()
