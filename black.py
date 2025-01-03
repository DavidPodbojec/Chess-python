import initial_state
from black_pieces.pawn import black_pawn_move
from black_pieces.rook import black_rook_move
from black_pieces.knight import black_knight_move
from black_pieces.king import black_king_move
from black_pieces.queen import black_queen_move
from black_pieces.bishop import black_bishop_move

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
        
    

