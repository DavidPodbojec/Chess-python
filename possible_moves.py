from black_pieces.pawn import black_pawn_move
from black_pieces.rook import black_rook_move
from black_pieces.knight import black_knight_move
from black_pieces.king import black_king_move
from black_pieces.queen import black_queen_move
from black_pieces.bishop import black_bishop_move
from white_pieces.pawn import white_pawn_move
from white_pieces.rook import white_rook_move
from white_pieces.knight import white_knight_move
from white_pieces.bishop import white_bishop_move
from white_pieces.queen import white_queen_move
from white_pieces.king import white_king_move

def black_possible_moves(board, selected_piece):
    
    possible_moves = []    

    piece = board[selected_piece[0]][selected_piece[1]]

    if piece == 11:
        black_king_move(board, selected_piece, possible_moves)
    elif piece == 21:
        black_queen_move(board, selected_piece, possible_moves)
    elif piece == 31:
        black_bishop_move(board, selected_piece, possible_moves)
    elif piece == 41:
        black_knight_move(board, selected_piece, possible_moves)
    elif piece == 51:
        black_rook_move(board, selected_piece, possible_moves)
    elif piece == 61:
        black_pawn_move(board, selected_piece, possible_moves)
        
    return possible_moves

def white_possible_moves(board, selected_piece):
    
    possible_moves = []           
               
    piece = board[selected_piece[0]][selected_piece[1]]
    
    if piece == 10:
        white_king_move(board, selected_piece, possible_moves)
    elif piece == 20:
        white_queen_move(board, selected_piece, possible_moves)
    elif piece == 30:
        white_bishop_move(board, selected_piece, possible_moves)
    elif piece == 40:
        white_knight_move(board, selected_piece, possible_moves)
    elif piece == 50:
        white_rook_move(board, selected_piece, possible_moves)
    elif piece == 60:
        white_pawn_move(board, selected_piece, possible_moves)
    
    return possible_moves


    

