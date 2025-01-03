def white_bishop_move(board, selected_piece, possible_moves):
    #down left
    if selected_piece[0] != 7 and selected_piece[1] != 0:
        count = 2
        if min(8-selected_piece[0], selected_piece[1]+1) > 1:
            count = min(8-selected_piece[0], selected_piece[1]+1)
            
        
        for i in range(1, count):
            if board[selected_piece[0]+i][selected_piece[1]-i] == 0: 
                possible_moves.append([selected_piece[0]+i, selected_piece[1]-i])
            elif board[selected_piece[0]+i][selected_piece[1]-i] % 10 != 0:
                possible_moves.append([selected_piece[0]+i, selected_piece[1]-i])
                break                   
            
            else:
                break
        
    #down right  
    if selected_piece[0] != 7 and selected_piece[1] != 7:
        count = 2
        
        if min(8-selected_piece[0], 8-selected_piece[1]) > 1:
            count = min(8-selected_piece[0], 8- selected_piece[1])
        
        for i in range(1, count):
            if board[selected_piece[0]+i][selected_piece[1]+i] == 0: 
                possible_moves.append([selected_piece[0]+i, selected_piece[1]+i])
            elif board[selected_piece[0]+i][selected_piece[1]+i] % 10 != 0:
                possible_moves.append([selected_piece[0]+i, selected_piece[1]+i])
                break
                
            else:
                break
                
    #up left
    if selected_piece[0] != 0 and selected_piece[1] != 0:
        count = 2
        if min(selected_piece[0]+1, selected_piece[1]+1) > 1:
            count = min(selected_piece[0]+1, selected_piece[1]+1)
        
        for i in range(1, count):
            
            if board[selected_piece[0]-i][selected_piece[1]-i] == 0:
                possible_moves.append([selected_piece[0]-i, selected_piece[1]-i])
            elif board[selected_piece[0]-i][selected_piece[1]-i] % 10 != 0:
                possible_moves.append([selected_piece[0]-i, selected_piece[1]-i])
                break
                
            else:
                break
                
    #up right 
    if selected_piece[0] != 0 and selected_piece[1] != 7:
        count = 2
        if min(selected_piece[0]+1, 8-selected_piece[1]) > 1:
            count = min(selected_piece[0]+1, 8-selected_piece[1])
        
        
        for i in range(1, count):
            if board[selected_piece[0]-i][selected_piece[1]+i] == 0:
                possible_moves.append([selected_piece[0]-i, selected_piece[1]+i])
            elif board[selected_piece[0]-i][selected_piece[1]+i] % 10 != 0:
                possible_moves.append([selected_piece[0]-i, selected_piece[1]+i])
                break

            else:
                break
            
    return possible_moves