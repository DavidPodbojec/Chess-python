import initial_state

def black_pawn_move(board, selected_piece, possible_moves):
    #pawn one move up
    if board[selected_piece[0]+1][selected_piece[1]] == 0:
        possible_moves.append([selected_piece[0]+1, selected_piece[1]])
        
    #two moves up
    if selected_piece[0] == 1 and board[selected_piece[0]+2][selected_piece[1]] == 0 and board[selected_piece[0]+1][selected_piece[1]] == 0:
        possible_moves.append([selected_piece[0]+2, selected_piece[1]])
    
    #take right
    if selected_piece[1] != 7 and board[selected_piece[0]+1][selected_piece[1]+1] != 0 and board[selected_piece[0]+1][selected_piece[1]+1] % 10 == 0:
        possible_moves.append([selected_piece[0]+1, selected_piece[1]+1])
        
    #take left
    if  selected_piece[1] != 0 and board[selected_piece[0]+1][selected_piece[1]-1] != 0 and board[selected_piece[0]+1][selected_piece[1]-1] % 10 == 0:
        possible_moves.append([selected_piece[0]+1, selected_piece[1]-1]) 

    if initial_state.white_pawn_2 == 1 and selected_piece[1] > 0:
        
        if initial_state.white_pawn_pos == (selected_piece[0], selected_piece[1]-1):
            possible_moves.append([selected_piece[0]+1,selected_piece[1]-1])

    if initial_state.white_pawn_2 == 1 and selected_piece[1] < 7:
    
        if initial_state.white_pawn_pos == (selected_piece[0], selected_piece[1]+1):
            possible_moves.append([selected_piece[0]+1, selected_piece[1]+1])
        
    return possible_moves