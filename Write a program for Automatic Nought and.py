import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def is_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(all(cell != ' ' for cell in row) for row in board)

def make_move(board, player, row, col):
    if board[row][col] == ' ':
        board[row][col] = player
        return True
    return False

def get_empty_cells(board):
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    return empty_cells

def computer_move(board):
    empty_cells = get_empty_cells(board)
    if empty_cells:
        return random.choice(empty_cells)
    return None

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    current_player = random.choice(players)

    while True:
        print_board(board)
        if is_winner(board, current_player):
            print(f'{current_player} wins!')
            break
        elif is_board_full(board):
            print('It\'s a tie!')
            break

        if current_player == 'X':
            row, col = map(int, input('Enter your move (row and column, separated by a space): ').split())
            if make_move(board, current_player, row, col):
                current_player = 'O'
        else:
            move = computer_move(board)
            if move:
                row, col = move
                print(f'Computer plays at row {row}, column {col}')
                make_move(board, current_player, row, col)
                current_player = 'X'

if __name__ == "__main__":
    main()
 