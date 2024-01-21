import numpy as np
# pip3 import numpy in terminal

ROW_COUNT = 6
COLUMN_COUNT = 7
# capitalized to show it is a non-changing variable

def create_board():
    board = np.zeros((ROW_COUNT,COLUMN_COUNT))
    return board
# creates a matrix (which will be our board)

def place_piece(board, row, column, piece):
    board[row][column] = piece

def is_valid(board, column):
    # will check if where piece is put is valid ie. top row should always remain at 0 otherwise whole column would be filled
    return board[ROW_COUNT-1][column] == 0

def get_next_open_row(board, column):
    for r in range(ROW_COUNT):
        if board[r][column] == 0:
           return r 

def print_board(board):
    print(np.flip(board, 0))
    # in num.py will flip on the y axis so it looks like it is falling

def winning_move(board, piece):
    # check horizontal
    for c in range(COLUMN_COUNT-3):
        # subtracting 3 since you would be able to make a winning move on the last three columns
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True
            # indexing the columns in the matrix where a four in a row can occur

    # check vertical
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # check diagonal 1
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    # check diagonal 2
    for c in range(COLUMN_COUNT-3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True


board = create_board()
print_board(board)

board = create_board()
game_over = False
turn = 0
# initializes the board and game (the game will play until game_over boolean turns true)

while not game_over:
# want to ask for player 1 input then player 2 input
    if turn == 0:
        column = int(input("Player 1, your turn! (0-6)"))

        if is_valid(board, column):
            row = get_next_open_row(board, column)
            place_piece(board, row, column, 1)

            if winning_move(board, 1):
                print("Player 1 Wins!!")
                game_over = True

    else: 
        column = int(input("Player 2, your turn! (0-6)"))

        if is_valid(board, column):
            row = get_next_open_row(board, column)
            place_piece(board, row, column, 2)

            if winning_move(board, 2):
                print("Player 2 Wins!!")
                game_over = True
                break
                # break so the board won't show up again after the winning_move

    print_board(board)

    turn += 1
    # after each go the turn will increase by one
    turn = turn % 2
    # will allow it to alternate between player 1 and player 2 turn

    # used: operators, variable, booloean, strings, integer, loops, functions, lists
    # didn't use: dictionaries in particular, could be implemented instead of def to sotre key:value pairs? 
    # tutorials used: https://www.youtube.com/watch?v=QUT1VHiLmmI (specifically 11.09-15.58) and https://www.youtube.com/watch?v=XGf2GcyHPhc&t=5697s (where I got the idea of conncect for) (referenced each time I got stuck, and to ensure my final code was correct)
