import initial_state
from check import white_is_check, black_is_check

def white_real_move(board, selected_piece, selected_square):
    piece = board[selected_piece[0]][selected_piece[1]]

    if piece == 60 and selected_piece[0] == 6 and selected_square[0] == 4:
        initial_state.white_pawn_2 = 1
        initial_state.white_pawn_pos = selected_square
    
    elif piece == 60:
        initial_state.white_pawn_2 = 0

    if piece == 60 and initial_state.black_pawn_2 == 1 and (initial_state.black_pawn_pos[0]-1, initial_state.black_pawn_pos[1]) == (selected_square[0], selected_square[1]):
        board[initial_state.black_pawn_pos[0]][initial_state.black_pawn_pos[1]] = 0
        
    
    if piece == 10:
        
        #improve caste so that it can't be done when a piece is checked
        if initial_state.white_king_moved == 0 and selected_square == (7, 2) and initial_state.white_rook1_moved == 0:
            if white_is_check(board, [7, 2]) or white_is_check(board, [7, 3]) or white_is_check(board, [7, 4]):
                pass
            else:
                initial_state.white_king_moved = 1
                initial_state.white_rook1_moved = 1
                board[7][0] = 0
                board[7][3] = 50

          
        elif initial_state.white_king_moved == 0 and selected_square == (7, 6) and initial_state.white_rook2_moved == 0:
            if white_is_check(board, [7, 6]) or white_is_check(board, [7, 5]) or white_is_check(board, [7, 4]):
                pass
            else:
                initial_state.white_king_moved = 1
                initial_state.white_rook2_moved = 1
                board[7][7] = 0
                board[7][5] = 50
                
        else:
            initial_state.white_king_moved = 1
    
    if piece == 50 and selected_piece == (7, 0):
        initial_state.white_rook1_moved = 1
    
    if piece == 50 and selected_piece == (7, 7):
        initial_state.white_rook2_moved = 1
        
    
    
    board[selected_piece[0]][selected_piece[1]] = 0
    board[selected_square[0]][selected_square[1]] = piece
    return board

def black_real_move(board, selected_piece, selected_square):
    
    piece = board[selected_piece[0]][selected_piece[1]]
    
    if piece == 61 and selected_piece[0] == 1 and selected_square[0] == 3:
        initial_state.black_pawn_2 = 1
        initial_state.black_pawn_pos = selected_square
        
    elif piece == 61:
        initial_state.black_pawn_2 = 0
        
    if piece == 61 and initial_state.white_pawn_2 == 1 and (initial_state.white_pawn_pos[0]+1, initial_state.white_pawn_pos[1]) == (selected_square[0], selected_square[1]):
        board[initial_state.white_pawn_pos[0]][initial_state.white_pawn_pos[1]] = 0
        

    if piece == 11:
        
        #improve caste so that it can't be done when a piece is checked
        if initial_state.black_king_moved == 0 and selected_square == (0, 2) and initial_state.black_rook1_moved == 0:
            if black_is_check(board, [0, 2]) or black_is_check(board, [0, 3]) or black_is_check(board, [0, 4]):
                pass
            else:
                initial_state.black_king_moved = 1
                initial_state.black_rook1_moved = 1
                board[0][0] = 0
                board[0][3] = 51

          
        elif initial_state.black_king_moved == 0 and selected_square == (0, 6) and initial_state.black_rook2_moved == 0:
            if black_is_check(board, [0, 6]) or black_is_check(board, [0, 5]) or black_is_check(board, [0, 4]):
               pass
            else:
                initial_state.black_king_moved = 1
                initial_state.black_rook2_moved = 1
                board[0][7] = 0
                board[0][5] = 51
        else:
            initial_state.black_king_moved = 1
    
    if piece == 51 and selected_piece == (0, 0):
        initial_state.black_rook1_moved = 1
    
    if piece == 51 and selected_piece == (0, 7):
        initial_state.black_rook2_moved = 1
        
    
    
    board[selected_piece[0]][selected_piece[1]] = 0
    board[selected_square[0]][selected_square[1]] = piece
    return board