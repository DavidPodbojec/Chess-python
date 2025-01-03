def black_knight_move(board, selected_piece, possible_moves):
    #down left
    if selected_piece[0] <= 5 and selected_piece[1] >= 1 and board[selected_piece[0]+2][selected_piece[1]-1] % 10 == 0:
        possible_moves.append([selected_piece[0]+2, selected_piece[1]-1]) 
        
    #down right
    if selected_piece[0] <= 5 and selected_piece[1] <= 6 and board[selected_piece[0]+2][selected_piece[1]+1] % 10 == 0:
        possible_moves.append([selected_piece[0]+2, selected_piece[1]+1]) 
        
    #left up
    if selected_piece[0] >= 1 and selected_piece[1] >= 2 and board[selected_piece[0]-1][selected_piece[1]-2] % 10 == 0:
        possible_moves.append([selected_piece[0]-1, selected_piece[1]-2])
        
    #left down
    if selected_piece[0] <= 6 and selected_piece[1] >= 2 and board[selected_piece[0]+1][selected_piece[1]-2] % 10 == 0:
        possible_moves.append([selected_piece[0]+1, selected_piece[1]-2])
        
    #right up
    if selected_piece[0] >= 1 and selected_piece[1] <= 5 and board[selected_piece[0]-1][selected_piece[1]+2] % 10 == 0:
        possible_moves.append([selected_piece[0]-1, selected_piece[1]+2])
        
    #right down
    if selected_piece[0] <= 6 and selected_piece[1] <= 5 and board[selected_piece[0]+1][selected_piece[1]+2] % 10 == 0:
        possible_moves.append([selected_piece[0]+1, selected_piece[1]+2])
        
    #up left
    if selected_piece[0] >= 2 and selected_piece[1] >= 1 and board[selected_piece[0]-2][selected_piece[1]-1] % 10 == 0:
        possible_moves.append([selected_piece[0]-2, selected_piece[1]-1])
        
    #up right 
    if selected_piece[0] >= 2 and selected_piece[1] <= 6 and board[selected_piece[0]-2][selected_piece[1]+1] % 10 == 0:
        possible_moves.append([selected_piece[0]-2, selected_piece[1]+1])
    
    
    return possible_moves