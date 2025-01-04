import initial_state

def white_pawn_move(board, selected_piece, possible_moves):
    #move one up
    if board[selected_piece[0]-1][selected_piece[1]] == 0:
        possible_moves.append([selected_piece[0]-1, selected_piece[1]])
    
    #move two up
    if selected_piece[0] == 6 and board[selected_piece[0]-2][selected_piece[1]] == 0 and board[selected_piece[0]-1][selected_piece[1]] == 0:
        possible_moves.append([selected_piece[0]-2, selected_piece[1]])
    
    #take right
    if selected_piece[1] != 7 and board[selected_piece[0]-1][selected_piece[1]+1] % 10 != 0:
        possible_moves.append([selected_piece[0]-1, selected_piece[1]+1])
    
    #take left
    if selected_piece[1] != 0 and board[selected_piece[0]-1][selected_piece[1]-1] % 10 != 0:
        possible_moves.append([selected_piece[0]-1, selected_piece[1]-1])
    
    if initial_state.black_pawn_2 == 1 and selected_piece[1] > 0:
        
        if initial_state.black_pawn_pos == (selected_piece[0], selected_piece[1]-1):
            possible_moves.append([selected_piece[0]-1,selected_piece[1]-1])

    if initial_state.black_pawn_2 == 1 and selected_piece[1] < 7:
    
        if initial_state.black_pawn_pos == (selected_piece[0], selected_piece[1]+1):
            possible_moves.append([selected_piece[0]-1, selected_piece[1]+1])



    return possible_moves