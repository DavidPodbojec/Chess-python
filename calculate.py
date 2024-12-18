from white import white_move
from black import black_move

def calculate(board, selected_piece):
    y, x = selected_piece
    piece = board[y][x]
    if piece!= 0 and piece%10==0:
        white_move(board, selected_piece)
    elif piece != 0:
        black_move(board, selected_piece)

    
