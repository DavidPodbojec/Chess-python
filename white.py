import initial_state
from white_pieces.pawn import white_pawn_move
from white_pieces.rook import white_rook_move
from white_pieces.knight import white_knight_move
from white_pieces.bishop import white_bishop_move
from white_pieces.queen import white_queen_move
from white_pieces.king import white_king_move

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

