from white import white_possible_moves
from black import black_possible_moves

def calculate(board, selected_piece):
    possible_moves = []
    y, x = selected_piece
    piece = board[y][x]
    if piece!= 0 and piece%10==0:
        possible_moves = white_possible_moves(board, selected_piece)
    elif piece != 0:
        possible_moves = black_possible_moves(board, selected_piece)

    return possible_moves

def move(board, selected_piece, selected_square, turn):
    if turn % 10 == 0:
        print("hello there white")
    else:
        print("hello there black")
