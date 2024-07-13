import random

def initialize_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    return None

def random_move(board):
    empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == ' ']
    return random.choice(empty_cells)

def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == 'X':
        return -1
    elif winner == 'O':
        return 1
    elif not any(' ' in row for row in board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for r in range(3):
            for c in range(3):
                if board[r][c] == ' ':
                    board[r][c] = 'O'
                    score = minimax(board, depth + 1, False)
                    board[r][c] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for r in range(3):
            for c in range(3):
                if board[r][c] == ' ':
                    board[r][c] = 'X'
                    score = minimax(board, depth + 1, True)
                    board[r][c] = ' '
                    best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -float('inf')
    move = None
    for r in range(3):
        for c in range(3):
            if board[r][c] == ' ':
                board[r][c] = 'O'
                score = minimax(board, 0, False)
                board[r][c] = ' '
                if score > best_score:
                    best_score = score
                    move = (r, c)
    return move

def main():
    board = initialize_board()
    player_turn = True  # True if it's the player's turn, False if it's the AI's turn

    while True:
        print_board(board)
        if player_turn:
            row, col = map(int, input("Enter your move (row and column): ").split())
            if board[row][col] == ' ':
                board[row][col] = 'X'
                if check_winner(board):
                    print("Player wins!")
                    break
                player_turn = False
        else:
            row, col = best_move(board)
            board[row][col] = 'O'
            if check_winner(board):
                print_board(board)
                print("AI wins!")
                break
            player_turn = True

        if not any(' ' in row for row in board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()
